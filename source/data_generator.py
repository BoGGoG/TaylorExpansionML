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

def random_func_and_taylor(x_x0, consts, amount=1, max_depth=4, taylor_order=4):
    x = x_x0[0]
    x0 = x_x0[1]
    random_functions = generate_random_functions([x], consts, amount=amount, max_depth=max_depth)
    rnd_fs = []
    rnd_fs_taylor = []
    rnd_fs_taylor_coeffs = []

    for f in random_functions:
        f_taylor = taylor(f, x0, taylor_order, x)
        if f_taylor != sympy.nan and not f_taylor.has(oo, -oo, zoo, sympy.nan):
            rnd_fs.append(f)
            rnd_fs_taylor.append(f_taylor)
            coeffs = sympy.Poly(f_taylor, x).all_coeffs()
            coeffs.reverse()
            rnd_fs_taylor_coeffs.append(coeffs)
    return [rnd_fs, rnd_fs_taylor, rnd_fs_taylor_coeffs]
