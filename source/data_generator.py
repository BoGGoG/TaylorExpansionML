import sys
import sympy
from sympy import symbols, srepr, series, oo, zoo
sys.path.append('../RandomFunctionGenerator/source')
from RandomFunctionGenerator import generate_random_functions

def factorial(n):
    if n <= 0:
        return 1
    else:
        return n * factorial(n - 1)

def taylor(function, x0, n, x = sympy.Symbol('x')):
    i = 0
    p = 0
    while i <= n:
        p = p + (function.diff(x, i).subs(x, x0))/(factorial(i))*(x - x0)**i
        i += 1
    return p

def random_func_and_taylor(x, consts, amount=1, max_depth=4):
    return 0
