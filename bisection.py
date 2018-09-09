from function_box import f
from error_box import relative_error
from write_archive import write_data
from graphic import generate_plot

# Recebe como parâmetros os valores do intervalo (a, b) e da precisão
def bisection(a, b, eps, func=f):
	#Lista usada para salvar os dados a serem escritos em um arquivo
	plot_data = []
    # Se a amplitude do intervalo atinge a precisão requerida, d = média(a, b)
	if (b - a) < eps:
        #return (a + b) * 0.5
		ans = (a + b) * 0.5
    # M recebe f(a), sendo a o do intervalo inicial
	M = f(a)

    # x_aprox recebe o valor aproximado de x
	x_aprox = 0

    # Número de iterações k vai de 1 a 1000 ou até encontrar a raiz d
	for k in range(1, 1001):
        # A aproximação x recebe a média da soma de a e b
		x = (a + b) * 0.5
    
		if(k > 1):
            # Calcula o erro relativo
			relative_e = relative_error(x,x_aprox)
			# Adiciona dados a serem escritos
			plot_data.append((x, relative_e))
        # Se a multiplicação de M por f(x) for maior que zero, atualiza-se
        # o valor de a
		if (M * func(x)) > 0:
			a = x
            # Se a diferença entre b e a for menor que o erro, ou seja, se a
            # amplitude do intervalo atinge a precisão requerida,
            # d = média(a, b)
			if (b - a) < eps:
                		#return (a + b) * 0.5
				ans = (a + b) * 0.5
        # Se o resultado da multiplicação não for maior que zero, atualiza-se b
        # e passa-se para a próxima iteração
		else:
			b = x

        # Recebe a raiz obtida na iteração usar no erro absoluto 
        # da proxima iteração
		x_aprox = x
	# Cria o arquivo a ser usado para os dados da bisseção
	File = open("Bisection", "w")
	File.close()    
	# Escreve dados no arquivo
	write_data(plot_data, "Bisection")
	# Gera plot dos dados
	generate_plot("Bisection")
	# Retorna a resposta
	return ans
