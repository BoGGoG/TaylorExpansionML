import sys
import sympy
from sympy import symbols, srepr, series, oo, zoo
sys.path.append('../../RandomFunctionGenerator/source')
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

x = symbols('x')
consts = symbols('a b c d')


rnd_fs_amount = 5
random_functions = generate_random_functions([x], consts, amount=rnd_fs_amount, max_depth=4)

rnd_fs = []
rnd_fs_taylor = []
rnd_fs_taylor_coeffs = []

# print(type(taylor(random_functions[0], 0, 4, x)))

x0 = 0
order = 4
for f in random_functions:
    f_taylor = taylor(f, x0, order, x)
    if f_taylor != sympy.nan and not f_taylor.has(oo, -oo, zoo, sympy.nan):
        rnd_fs.append(f)
        rnd_fs_taylor.append(f_taylor)
        coeffs = sympy.Poly(f_taylor, x).all_coeffs()
        coeffs.reverse()
        rnd_fs_taylor_coeffs.append(coeffs)

for i in range(len(rnd_fs)):
    print("-----------")
    print("f:", rnd_fs[i])
    print("taylor:", rnd_fs_taylor[i])
    print("coeffs:", rnd_fs_taylor_coeffs[i])


