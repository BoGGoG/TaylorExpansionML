import os
import sys
import inspect
from icecream import ic
import sympy as sp
import pytest

script_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
root_dir = os.path.dirname(script_dir)
sys.path.insert(0, root_dir)


from source.data_preparation import format_integer, unformat_integer, sympy_to_prefix, prefix_to_sympy


def test_unformat_integer():
    test_int1 = sp.parsing.parse_expr("1")
    test_int2 = sp.parsing.parse_expr("2")
    test_int3 = sp.parsing.parse_expr("0")
    test_int4 = sp.parsing.parse_expr("-1")
    test_int5 = sp.parsing.parse_expr("-1234")
    test_int6 = sp.parsing.parse_expr("+1234")

    test_int_formated1 = format_integer(test_int1)
    test_int_formated2 = format_integer(test_int2)
    test_int_formated3 = format_integer(test_int3)
    test_int_formated4 = format_integer(test_int4)
    test_int_formated5 = format_integer(test_int5)
    test_int_formated6 = format_integer(test_int6)

    test_int_recovered1 = unformat_integer(test_int_formated1)
    test_int_recovered2 = unformat_integer(test_int_formated2)
    test_int_recovered3 = unformat_integer(test_int_formated3)
    test_int_recovered4 = unformat_integer(test_int_formated4)
    test_int_recovered5 = unformat_integer(test_int_formated5)
    test_int_recovered6 = unformat_integer(test_int_formated6)

    assert test_int1 == test_int_recovered1
    assert test_int2 == test_int_recovered2
    assert test_int3 == test_int_recovered3
    assert test_int4 == test_int_recovered4
    assert test_int5 == test_int_recovered5
    assert test_int6 == test_int_recovered6

    assert test_int2 != test_int_recovered1

def test_prefix_to_sympy():
    expr0 = sp.parsing.parse_expr("x+y+sin(3)")
    expr1 = sp.parsing.parse_expr("x")
    expr2 = sp.parsing.parse_expr("1")
    expr3 = sp.parsing.parse_expr("x*y + 3")
    expr4 = sp.parsing.parse_expr("-42")
    # expr5 = sp.parsing.parse_expr("sin(cos(x**2))")
    expr5 = sp.parsing.parse_expr("0")
    expr6 = sp.parsing.parse_expr("x**2 / y + exp(-y**2 + abs(-2*x))")


    expr0_prefix = sympy_to_prefix(expr0)
    expr1_prefix = sympy_to_prefix(expr1)
    expr2_prefix = sympy_to_prefix(expr2)
    expr3_prefix = sympy_to_prefix(expr3)
    expr4_prefix = sympy_to_prefix(expr4)
    expr5_prefix = sympy_to_prefix(expr5)
    expr6_prefix = sympy_to_prefix(expr6)

    expr0_recovered = prefix_to_sympy(expr0_prefix)
    expr1_recovered = prefix_to_sympy(expr1_prefix)
    expr2_recovered = prefix_to_sympy(expr2_prefix)
    expr3_recovered = prefix_to_sympy(expr3_prefix)
    expr4_recovered = prefix_to_sympy(expr4_prefix)
    expr5_recovered = prefix_to_sympy(expr5_prefix)
    expr6_recovered = prefix_to_sympy(expr6_prefix)

    assert expr0 == expr0_recovered
    assert expr1 == expr1_recovered
    assert expr2 == expr2_recovered
    assert expr3 == expr3_recovered
    assert expr4 == expr4_recovered
    assert expr5 == expr5_recovered
    assert expr6 == expr6_recovered
