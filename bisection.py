from function_box import f
from error_box import re_per_method
from write_archive import write_data
from graphic import generate_plot

# Recebe como parâmetros os valores do intervalo (a, b) e da precisão
def bisection(a, b, eps, func = f):
    # Inicializa a lista onde serão salvas as aproximações de d
	iter_values = []

    # Se a amplitude do intervalo atinge a precisão requerida, d = média(a, b)
	if (b - a) < eps:
		iter_values.append((a + b) * 0.5)
		ans = iter_values

    # M recebe f(a), sendo a o do intervalo inicial
	M = f(a)

    # Número de iterações k vai de 1 a 1000 ou até encontrar a raiz d
	for k in range(1, 1001):
        # A aproximação d recebe a média da soma de a e b
		d = (a + b) * 0.5
            
        # Se a multiplicação de M por f(d) for maior que zero, atualiza-se
        # o valor de a
		if (M * func(d)) > 0:
			a = d
            # Se a diferença entre b e a for menor que o erro, ou seja, se a
            # amplitude do intervalo atinge a precisão requerida,
            # d = média(a, b)
			if (b - a) < eps:
				iter_values.append((a + b) * 0.5)
				ans = iter_values
        # Se o resultado da multiplicação não for maior que zero, atualiza-se b
        # e passa-se para a próxima iteração
		else:
			iter_values.append(d)
			b = d
	re_values = re_per_method(iter_values)
	File = open("Bisection", "w")
	File.close()
	write_data(iter_values, re_values, "Bisection")
	generate_plot("Bisection")
	return ans	

