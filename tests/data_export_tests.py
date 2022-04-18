# data export tests
import sys

import sympy
import os
from sympy import symbols, srepr, series, oo, zoo
from icecream import ic
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from source.data_generator import random_func_and_taylor, export_functions_and_taylor

x = symbols('x')
consts = symbols('a b c d')
rnd_fs_amount = 40
x0 = 0
taylor_order = 4

rnd_fs, rnd_fs_taylor, rnd_fs_taylor_coeffs = random_func_and_taylor([x, x0], consts, amount=rnd_fs_amount,
    max_depth=4, taylor_order=taylor_order, verbose=False)

ic(len(rnd_fs) == rnd_fs_amount)

_ = export_functions_and_taylor([rnd_fs, rnd_fs_taylor, rnd_fs_taylor_coeffs], "tests/data_tests.nosync/train.csv", verbose=True)
try:
    _ = export_functions_and_taylor([rnd_fs, rnd_fs_taylor, rnd_fs_taylor_coeffs], "tests/data_tests.nosync/train.csv", verbose=True, representation_type="banana")
except ValueError as err:
    print("ValueError:", err)
