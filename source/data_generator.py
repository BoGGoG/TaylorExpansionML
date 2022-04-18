import sys
import os
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
    Usually a random function won't have a well defined Taylor expansion. If this happens, then a new function will be generated.

    Arguments:
        - `x_x0`: [x, x0] where x is the sympy symbol of the variable of the functions. x0 is the expansion point
        - `consts`: sympy symbols of constants that should be randomly distributed in the functions
        - `amount=1`: how many random functions you want
        - `max_depth=4`: how deep functions should be nested. sin(cos(exp(x)))
        - `verbose=False`: If you want internal information to be printed.

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

def export_functions_and_taylor(fs_and_taylor, filename, verbose=True, representation_type="str"):
    """
    Save the functions and its taylor expansions in a .csv file
    Will create 3 files:
        - `filename.extension`: The file that contains the functions with the extension you chose
        - `filename_taylor.extensions`: The taylor expansions
        - `filename_taylor_coeffs.extensions`: The taylor expansions


    Arguments:
        - `fs_and_taylor`: [fs, taylors, taylor_coeffs] the functions, their taylor expansion and the coefficients of the expansion
        - `filename`: The name of the file that the functions should be exportet to
        - `verbose:True`: If you want internal information to obe printed
        -`representation_type="str"`: Do you want the functions exported as strings (`"str"`) or as sympy srepr form (`"srepr"`)
    """
    fs, taylors, taylor_coeffs = fs_and_taylor
    file_no_extension, extension = os.path.splitext(filename)
    taylor_file_name = file_no_extension+"_taylor"+extension
    coeffs_file_name = file_no_extension+"_coeffs"+extension
    fs_file = open(filename, "a")
    taylor_file = open(taylor_file_name , "a")
    coeffs_file = open(coeffs_file_name, "a")
    if verbose:
        print("len(fs):", len(fs))
        print("functions file: ", filename)
        print("taylor file: ", taylor_file_name)
        print("coeffs file: ", coeffs_file_name)
    for i in range(len(fs)):
        if verbose: print("exporting function number", i)

        if representation_type == "srepr":
            fs_file.write(srepr(fs[i])+"\n")
            taylor_file.write(srepr(taylors[i])+"\n")
            coeffs_file.write(srepr(taylor_coeffs[i])+"\n")
        elif representation_type == "str":
            fs_file.write(str(fs[i])+"\n")
            taylor_file.write(str(taylors[i])+"\n")
            coeffs_file.write(str(taylor_coeffs[i])+"\n")
        else:
            raise ValueError("representation_type="+representation_type+" is not valid. Choose 'str' or 'srepr" )

    fs_file.close()
    taylor_file.close()
    coeffs_file.close()
    return 0
