import sympy
from sympy import *
import numpy as np


def pad_right(list, total_length=4, const=0):
    length = len(list)
    values_needed = total_length - length 
    if values_needed > 0:
        return np.pad(list, (0, values_needed), mode="constant", constant_values=const) 
    else:
        return list[0:total_length]

def sympy_tokenize(expr, tokens_list=[], depth=0, parent_ind=None):
    if (expr.func == sympy.core.symbol.Symbol) | (expr.func == sympy.core.numbers.Integer):
        to_append = expr
    else:
        to_append = expr.func
    tokens_list.append(to_append)
    for ind, arg in enumerate(expr.args):
        sympy_tokenize(arg, tokens_list, depth+1, parent_ind=ind)
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