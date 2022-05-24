import os
import sys
import inspect
from icecream import ic
import sympy
from sympy.parsing.sympy_parser import repeated_decimals

script_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
root_dir = os.path.dirname(script_dir)
sys.path.insert(0, root_dir)


from source.data_preparation import sympy_tokenize, sympy_tokenize_str, vectorize_ds, vectorize_sentence, pad_right, sympy_to_prefix, repeat_operator_until_correct_binary
x = sympy.Symbol("x")
expr0a = sympy.parsing.parse_expr("x")
expr0b = sympy.parsing.parse_expr("1")
expr0c = sympy.parsing.parse_expr("2")
expr0d = sympy.parsing.parse_expr("sin(x)")
expr0e = sympy.parsing.parse_expr("sin(cos(x))")
expr0f = sympy.parsing.parse_expr("tan(sin(cos(x)))")
expr1a = sympy.parsing.parse_expr("x + sin(y+z)")
expr1b = sympy.parsing.parse_expr("x + sinh(cos(x**2)) + 3")
expr1c = sympy.parsing.parse_expr("x + sinh(cos(x**2)) + 3 + 1 + exp(3)")
expr2a = sympy.parsing.parse_expr("abs(y) + cot(x)")
expr2b = sympy.parsing.parse_expr("1/x + acsc(1+x+asec(y))")
expr2c = sympy.parsing.parse_expr("sign(x) + ln(1/x) + exp(-x**2)")

# ic(repeat_operator_until_correct_binary("sin", ["x"]))
# ic(repeat_operator_until_correct_binary("mul", ["x", "y", "z"]))
# ic(repeat_operator_until_correct_binary("mul", ["a", "x", "y", "z"]))
# ic(repeat_operator_until_correct_binary("add", ["a", "x", "y", "z"]))
# ic(repeat_operator_until_correct_binary("add", ["a", "x"]))
# ic(repeat_operator_until_correct_binary("add", ["a", "x", ["sin", "x"]]))

# ic(expr)
# ic(type(expr.args))
# ic(expr.args)
# ic(sympy_to_prefix(expr))

ic(expr0a)
ic(expr0b)
ic(expr0c)
ic(expr0d)
ic(expr0e)
ic(expr0f)

ic(expr1a)
ic(expr1b)
ic(expr1c)

ic(expr2a)
ic(expr2b)
ic(expr2c)

# ic(expr0b)
# ic(expr1)
# ic(expr2)
ic(sympy_to_prefix(expr0a))
ic(sympy_to_prefix(expr0b))
ic(sympy_to_prefix(expr0c))
ic(sympy_to_prefix(expr0d))
ic(sympy_to_prefix(expr0e))
ic(sympy_to_prefix(expr0f))

ic(sympy_to_prefix(expr1a))
ic(sympy_to_prefix(expr1b))
ic(sympy_to_prefix(expr1c))

ic(sympy_to_prefix(expr2a))
ic(sympy_to_prefix(expr2b))
ic(sympy_to_prefix(expr2c))

ic(x)
ic(str(x))


