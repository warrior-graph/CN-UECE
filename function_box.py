import math


def f(d, amp):
    return amp * math.exp(d) - 4 * d**2


def f_derived(d, amp):
    return amp * math.exp(d) - 8 * d
