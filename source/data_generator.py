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

def random_func_and_taylor(x_x0, consts, amount=1, max_depth=4, taylor_order=4, verbose=False):
    x = x_x0[0]
    x0 = x_x0[1]
    rnd_fs = []
    rnd_fs_taylor = []
    rnd_fs_taylor_coeffs = []

    while len(rnd_fs) < amount:
        f = generate_random_functions([x], consts, amount=1, max_depth=max_depth)[0]
        f_taylor = taylor(f, x0, taylor_order, x)
        if verbose: 
            print("generated function:", f)
            print("taylor:", f_taylor)
        if f_taylor != sympy.nan and not f_taylor.has(oo, -oo, zoo, sympy.nan):
            rnd_fs.append(f)
            rnd_fs_taylor.append(f_taylor)
            coeffs = sympy.Poly(f_taylor, x).all_coeffs()
            coeffs.reverse()
            rnd_fs_taylor_coeffs.append(coeffs)
        elif verbose:
            print("Function does not have taylor expansion, skipping.")
    return [rnd_fs, rnd_fs_taylor, rnd_fs_taylor_coeffs]
