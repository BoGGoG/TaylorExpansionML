from itertools import repeat
import sympy as sp
from sympy import *
import numpy as np
from icecream import ic

# operators and operators_nargs are from 
# https://github.com/facebookresearch/SymbolicMathematics

operators = {
    # Elementary functions
    sp.Add: 'add',
    sp.Mul: 'mul',
    sp.Pow: 'pow',
    sp.exp: 'exp',
    sp.log: 'ln',
    sp.Abs: 'abs',
    sp.sign: 'sign',
    # Trigonometric Functions
    sp.sin: 'sin',
    sp.cos: 'cos',
    sp.tan: 'tan',
    sp.cot: 'cot',
    sp.sec: 'sec',
    sp.csc: 'csc',
    # Trigonometric Inverses
    sp.asin: 'asin',
    sp.acos: 'acos',
    sp.atan: 'atan',
    sp.acot: 'acot',
    sp.asec: 'asec',
    sp.acsc: 'acsc',
    # Hyperbolic Functions
    sp.sinh: 'sinh',
    sp.cosh: 'cosh',
    sp.tanh: 'tanh',
    sp.coth: 'coth',
    sp.sech: 'sech',
    sp.csch: 'csch',
    # Hyperbolic Inverses
    sp.asinh: 'asinh',
    sp.acosh: 'acosh',
    sp.atanh: 'atanh',
    sp.acoth: 'acoth',
    sp.asech: 'asech',
    sp.acsch: 'acsch',
    # Derivative
    sp.Derivative: 'derivative',
}

operators_nargs = {
    # Elementary functions
    'add': 2,
    'sub': 2,
    'mul': 2,
    'div': 2,
    'pow': 2,
    'rac': 2,
    'inv': 1,
    'pow2': 1,
    'pow3': 1,
    'pow4': 1,
    'pow5': 1,
    'sqrt': 1,
    'exp': 1,
    'ln': 1,
    'abs': 1,
    'sign': 1,
    # Trigonometric Functions
    'sin': 1,
    'cos': 1,
    'tan': 1,
    'cot': 1,
    'sec': 1,
    'csc': 1,
    # Trigonometric Inverses
    'asin': 1,
    'acos': 1,
    'atan': 1,
    'acot': 1,
    'asec': 1,
    'acsc': 1,
    # Hyperbolic Functions
    'sinh': 1,
    'cosh': 1,
    'tanh': 1,
    'coth': 1,
    'sech': 1,
    'csch': 1,
    # Hyperbolic Inverses
    'asinh': 1,
    'acosh': 1,
    'atanh': 1,
    'acoth': 1,
    'asech': 1,
    'acsch': 1,
    # Derivative
    'derivative': 2,
    # custom functions
    'f': 1,
    'g': 2,
    'h': 3,
}

def flatten(l, ltypes=(list, tuple)):
    """
    flatten a python list
    from http://rightfootin.blogspot.com/2006/09/more-on-python-flatten.html
    """
    ltype = type(l)
    l = list(l)
    i = 0
    while i < len(l):
        while isinstance(l[i], ltypes):
            if not l[i]:
                l.pop(i)
                i -= 1
                break
            else:
                l[i:i + 1] = l[i]
        i += 1
    return ltype(l)


def pad_right(list, total_length=4, const=0):
    length = len(list)
    values_needed = total_length - length 
    if values_needed > 0:
        return np.pad(list, (0, values_needed), mode="constant", constant_values=const) 
    else:
        return list[0:total_length]

def sympy_tokenize(expr, tokens_list=[], depth=0):
    if (expr.func == sp.core.symbol.Symbol) | (expr.func == sp.core.numbers.Integer):
        to_append = expr
    else:
        to_append = expr.func
    tokens_list.append(to_append)
    for arg in expr.args:
        sympy_tokenize(arg, tokens_list, depth+1)
    return tokens_list

def sympy_tokenize_str(sentence):
    Xi_tokenized = sympy_tokenize(sentence, tokens_list=[])
    Xi_tokenized_str = [srepr(el) for el in Xi_tokenized]
    return Xi_tokenized_str

def key_to_index_lookup_safe(key_to_index, word, shift=0):
    """look up word in key_to_index, replace unknown with max_index+1"""
    number_of_keys = len(key_to_index)
    try:
        index = key_to_index[word]
    except:
        index = number_of_keys
    return index + shift

def vectorize_sentence(Xi, model):
    # 0 reserved for [end], so add 1 to index
    key_to_index = model.wv.key_to_index
    Xi_vectorized = [key_to_index_lookup_safe(key_to_index, word, shift=1) for word in Xi]
    return Xi_vectorized

def vectorize_ds(X_tokenized_str, model, sequence_length=25):
    X_vectorized = [ vectorize_sentence(sentence, model) for sentence in X_tokenized_str]
    # sequence_length = np.max([len(Xi) for Xi in X_vectorized]) + 5
    X_vectorized = [pad_right(Xi, sequence_length, const=0) for Xi in X_vectorized]
    return X_vectorized

atoms = [str, sp.core.symbol.Symbol, sp.core.Integer, sp.core.numbers.One, sp.core.numbers.NegativeOne]

def sympy_to_prefix(expression):
    """
    Recursively go from a sympy expression to a prefix notation.
    Returns a flat list of tokens.
    """
    return flatten(sympy_to_prefix_rec(expression, []))

def sympy_to_prefix_rec(expression, ret):
    """
    Recursively go from a sympy expression to a prefix notation.
    The operators all get converted to their names in the array `operators`.
    Returns a nested list, where the nesting basically stands for parentheses.
    Since in prefix notation with a fixed number of arguments for each function (given in `operators_nargs`),
    parentheses are not needed, we can flatten the list later.
    """
    f = expression.func
    if f in atoms:
        return ret+[expression]
    f_str = operators[f]
    f_nargs = operators_nargs[f_str]
    args = expression.args
    if len(args) == 1 & f_nargs == 1: 
        ret = ret + [f_str]
        return sympy_to_prefix_rec(args[0], ret)
    if len(args) == 2:
        ret = ret + [f_str, sympy_to_prefix_rec(args[0], []), sympy_to_prefix_rec(args[1], [])]
    if len(args) > 2:
        args = list(map(lambda x: sympy_to_prefix_rec(x, []), args))
        ret = ret + repeat_operator_until_correct_binary(f_str, args)
    return ret 

def repeat_operator_until_correct_binary(op, args, ret=[]):
    """
    sympy is not strict enough with the number of arguments.
    E.g. multiply takes a variable number of arguments, but for 
    prefix notation it needs to ALWAYS have exactly 2 arguments

    This function is only for binary operators.

    Here I choose the convention as follows:
        1 + 2 + 3 --> + 1 + 2 3 
    
    This is the same convention as in https://arxiv.org/pdf/1912.01412.pdf
    on page 15.

    input:
        op: in string form as in the list `operators`
        args: [arg1, arg2, ...] arguments of the operator, e.c. [1, 2, x**2,
                ...]. They can have other things to be evaluated in them
        ret: the list you already have. Usually []. Watch out, I think one has to explicitely give [],
            otherwise somehow the default value gets mutated, which I find a strange python behavior.
    """

    is_binary = operators_nargs[op] == 2
    assert is_binary, "repeat_operator_until_correct_binary only takes binary operators" 

    if len(args) == 0:
        return ret
    elif len(ret) == 0:
        ret = [op] + args[-2:]
        args = args[:-2]
    else:
        ret = [op] + args[-1:] + ret
        args = args[:-1]

    return repeat_operator_until_correct_binary(op, args, ret)

