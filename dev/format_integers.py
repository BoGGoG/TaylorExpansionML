"""
Format integers as in [the paper](https://arxiv.org/pdf/1912.01412.pdf) 
"""

import os
import sys
import inspect
from icecream import ic
import sympy
from sympy.parsing.sympy_parser import repeated_decimals
from sympy import srepr

script_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
root_dir = os.path.dirname(script_dir)
sys.path.insert(0, root_dir)


from source.data_preparation import sympy_tokenize, sympy_tokenize_str, vectorize_ds, vectorize_sentence, pad_right, sympy_to_prefix, repeat_operator_until_correct_binary, format_integer

test_int1 = sympy.parsing.parse_expr("1")
test_int2 = sympy.parsing.parse_expr("2")
test_int3 = sympy.parsing.parse_expr("0")
test_int4 = sympy.parsing.parse_expr("-1")
test_int5 = sympy.parsing.parse_expr("-1234")
test_int6 = sympy.parsing.parse_expr("+1234")

ic(type(test_int1))
ic(type(test_int2))
ic(type(test_int3))
ic(type(test_int4))
ic(type(test_int5))
ic(srepr(test_int1))
ic(test_int2)
ic(test_int3)
ic(type(sympy.Integer(1).__int__()))

ic(type(format_integer(test_int1)))
ic(format_integer(test_int1))
ic(format_integer(test_int2))
ic(format_integer(test_int3))
ic(format_integer(test_int4))
ic(format_integer(test_int5))
ic(format_integer(test_int6))

ic(sympy_to_prefix(test_int5))
