import pytest
from bisection import bisection
from secant import secant
from newton_raphson import newton_raphson

def func(x):
    return x**3 - 9*x + 3

def func_derived(x):
    return 3*x**2 - 9

# Compara os resultados com os exemplos do livro com 9 casas decimais
def test_methods():
    assert round(bisection(0, 1, 1e-3, func)[-1], 9) == 0.337402344
    assert round(newton_raphson(0.5, 1e-4, func, func_derived)[-1], 9) == 0.337606838
    assert round(secant(0, 1, 5e-4, func)[-1], 9) == 0.337634621 

