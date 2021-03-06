from isolation import isolation
from bisection import bisection
from secant import secant
from newton_raphson import newton_raphson
from error_box import re_per_method
from function_box import f, f_derived

from plot import dino_plot

import matplotlib.pyplot as plt
import numpy as np

# Recebe os valores de entrada n (número de movimentos), eps (precisão) e amp
# (amplitude de cada movimento), chama as funções responsáveis pelos cálculos
# dos métodos e organiza todos os dados numa lista que é passada como parâmetro
# para a função que plota os gráficos


def do():
    # Recebe número de movimentos e precisão
    n = int(input('Insert number of movements:\n'))
    eps = float(input('Insert precision(eps):\n'))

    # Para cada movimento
    for k in range(n):
        # Recebe o valor da amplitude
        amp = float(input(str(k + 1) + ': Insert amplitude:\n'))

        # Calcula o intervalo
        (a, b) = isolation(amp)
        

        # Inicializa lista que conterá os dados das tabelas dos 3 métodos
        data_list = []

        # Calcula e salva aproximações de d, abs(b - a) ou abs(dk - d[k-1]), f(d) e erros relativos
        bisection_data, bisection_abs_diff = zip(*bisection(a, b, eps, amp))
        bisection_applied = [f(x, amp) for x in bisection_data]
        bisection_re = re_per_method(bisection_data)
        data_list.append([bisection_data, bisection_applied, bisection_abs_diff, bisection_re])

        nr_data, nr_abs_diff = zip(*newton_raphson((a + b) * 0.5, eps, amp))
        nr_applied = [f(x, amp) for x in nr_data]
        nr_re = re_per_method(nr_data)
        data_list.append([nr_data, nr_applied, nr_abs_diff, nr_re])

        secant_data, secant_abs_diff = zip(*secant(a, b, eps, amp))
        secant_applied = [f(x, amp) for x in secant_data]
        secant_re = re_per_method(secant_data)
        data_list.append([secant_data, secant_applied, secant_abs_diff, secant_re])

        # Salva na lista os nomes dos métodos, valor da amplitude e intervalo (a, b)
        data_list.append((['Bisection', 'Newton-Raphson', 'Secant'], amp, a, b, eps))

        # Passa os dados para a função responsável pelas tabelas
        dino_plot(data_list)
