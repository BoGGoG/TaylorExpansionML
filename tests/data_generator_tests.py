# data generator tests

import sys
import sympy
import os
from sympy import symbols, srepr, series, oo, zoo

import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from source.data_generator import random_func_and_taylor 

x = symbols('x')
consts = symbols('a b c d')
rnd_fs_amount = 5


print(random_func_and_taylor(x, consts, amount=rnd_fs_amount, max_depth=4))
