import os
import sys
import inspect
from icecream import ic
import sympy
from sympy.parsing.sympy_parser import repeated_decimals

script_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
root_dir = os.path.dirname(script_dir)
sys.path.insert(0, root_dir)


from source.data_preparation import format_integer 

import pytest

def test_integers():
    test_int1 = sympy.parsing.parse_expr("1")
    test_int2 = sympy.parsing.parse_expr("2")
    test_int3 = sympy.parsing.parse_expr("0")
    test_int4 = sympy.parsing.parse_expr("-1")
    test_int5 = sympy.parsing.parse_expr("-1234")
    test_int6 = sympy.parsing.parse_expr("+1234")

    assert format_integer(test_int1) == ['int', 's+', '1']
    assert format_integer(test_int2) == ['int', 's+', '2']
    assert format_integer(test_int3) == ['int', 's+', '0']
    assert format_integer(test_int4) == ['int', 's-', '1']
    assert format_integer(test_int5) == ['int', 's-', '1', '2', '3', '4']
    assert format_integer(test_int6) == ['int', 's+', '1', '2', '3', '4']
    assert format_integer(test_int6) != ['int', 's-', '1', '2', '3', '4']


