from isolation import isolation
from bisection import bisection
from secant import secant
from newton_raphson import newton_raphson
from write_archive import write_data
from error_box import re_per_method
from function_box import f, f_derived

from plot import dino_plot

import matplotlib.pyplot as plt
import numpy as np


def do():
    # n = int(input('Insert number of movements:\n'))
    # eps = float(input('Insert precision(eps):\n'))
    n , eps = 1, 1e-5
    for k in range(n):
        # amp = float(input(str(k + 1) + ': Insert amplitude:\n'))
        amp = 1

        (a, b) = isolation(amp)
        rows = ('x', 'f(x)', 'Relative error')
        
        data_list = []

        bisection_data = bisection(a, b, eps, amp)
        bisection_re = re_per_method(bisection_data)
        bisection_applied = [f(x) for x in bisection_data]
        data_list.append([bisection_data, bisection_re, bisection_applied])
        
        nr_data = newton_raphson((a + b) * 0.5, eps, amp)
        nr_re = re_per_method(nr_data)
        nr_applied = [f(x) for x in nr_data]
        data_list.append([nr_data, nr_re, nr_applied])

        secant_data = secant(a, b, eps, amp)
        secant_re = re_per_method(secant_data)
        secant_applied = [f(x) for x in secant_data]
        data_list.append([nr_data, nr_re, nr_applied])
        
        dino_plot(data_list)

