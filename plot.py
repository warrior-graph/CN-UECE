import numpy as np
import matplotlib.pyplot as plt

# Plota as tabelas com os resultados das iterações dos 3 métodos:
# Bisseção, Newton-Raphson e Secante


def dino_plot(data_list):
    # Número da figura (0: bisection, 1: newton-raphson, 2: secant)
    k = 0

    # Configura os gráficos
    for data in data_list[:3]:
        fig = plt.figure(k)
        fig.patch.set_visible(False)
        plt.axis('off')

        # Título da tabela (método, fórmula, amplitude, intervalo, epsilon)
        plt.title('Method ' + data_list[-1][0][k] + '\n' +
                  r'$f(d) = amp \times e^d - 4 \times d^2$' + '\n' +
                  r'$amp = $' + str(data_list[-1][1]) +
                  r'$,\/I = [$' + str(data_list[-1][2]) + r'$, $' +
                  str(data_list[-1][3]) + r'$]$' +
                  r'$,\/\varepsilon = $' + str(data_list[-1][4]))

        # Títulos das colunas
        if k:
            columns = ('d', 'f(d)', r'$abs(d_k - d_{k-1})$', 'Relative error')
        else:
            columns = ('d', 'f(d)', 'abs(b - a)', 'Relative error')

        # Número de linhas (n) e colunas (m)
        n = len(data[0])
        m = len(data)

        # Exibe valor das iterações
        rows = [' ' + str(x) + ' ' for x in range(1, n + 1)]

        # Insere os dados nas células da tabela
        cell_text = []
        for i in range(n):
            aux = []
            for j in range(m):
                aux.append(data[j][i])
            cell_text.append(['%f' % x for x in aux])

        # Configura a tabela
        plt.table(cellText=cell_text,
                  rowLabels=rows,
                  colLabels=columns,
                  loc='center')
        fig.tight_layout()

        # Incrementa o número da figura
        k += 1

    # Exibe os 3 gráficos
    plt.show()
