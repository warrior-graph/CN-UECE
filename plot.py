import numpy as np
import matplotlib.pyplot as plt


def dino_plot(data_list):

    k = 0
    
    fig, ax = plt.subplots()
    
    ax.axis('off')
    ax.axis('tight')
    for data in data_list:
        k += 1
        fig.patch.set_visible(False)
        fig = plt.figure(k)
        fig.patch.set_visible(False)
        
        columns = ('x', 'f(x)', 'Relative error')
        n = len(data[0])
        m = len(data)

        rows = [' ' + str(x) + ' ' for x in range(1, n + 1)]

        cell_text = []
        n = len(data[0])
        m = len(data)
        for i in range(n):
            aux = []
            for j in range(m):
                aux.append(data[j][i])
            cell_text.append(['%1.5f' % x for x in aux])

        # Add a table at the bottom of the axes
        plt.table(cellText=cell_text,
                  rowLabels=rows,
                  colLabels=columns,
                  loc='center')

        # Adjust layout to make room for the table:
        # plt.subplots_adjust(left=0.2, bottom=0.2)

    plt.show()
