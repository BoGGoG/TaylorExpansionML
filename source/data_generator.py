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
    """
    Generate random functions according to the RandomFunctionGenerator module.

    Arguments:
        - `x_x0`: [x, x0] where x is the sympy symbol of the variable of the functions. x0 is the expansion point
        - `consts`: sympy symbols of constants that should be randomly distributed in the functions
        - `amount=1`: how many random functions you want
        - `max_depth=4`: how deep functions should be nested. sin(cos(exp(x)))

    Returns: [rnd_fs, rnd_fs_taylor, rnd_fs_taylor_coeffs] 
        - `rnd_fs`: the random functions in sympy srepr form
        - `rnd_fs_taylor`: the taylor expansion of the functions in sympy srepr form
        - `rnd_fs_taylor`: the coefficients of the taylor expansion of the functions in sympy srepr form
    """
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

def export_functions_and_taylor(fs_and_taylor, filename):
    """
    Save the functions and its taylor expansions in a .csv file

    Arguments:
        - `fs_and_taylor`: [fs, taylors, taylor_coeffs] the functions, their taylor expansion and the coefficients of the expansion
        - `filename`: The name of the file that the functions should be exportet to
    """
    fs, taylors, taylor_coeffs = fs_and_taylor
    print("len(fs):", len(fs))
    return 0
