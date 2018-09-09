from function_box import f, f_derived
from error_box import relative_error
from write_archive import write_data
from graphic import generate_plot

# Recebe como parâmetros o valor da aproximação inicial e a precisão
def newton_raphson(x0, eps, func=f, func_derived=f_derived):
	#Lista usada para salvar os dados a serem escritos em um arquivo
	plot_data = []

	# Se o módulo de f(x0) for menor que o erro, d = x0
	if abs(func(x0)) < eps:
		#return x0
		ans = x0
	# Inicializa xw com o valor da aproximação inicial
	xw = x0

	# Número de iterações k vai de 1 a 1000 ou até encontrar a raiz d
	for k in range(1, 1001):
		# Nova aproximação x1 é calculada a partir da função de iteração do
		# método com FL
		
		# Valor aproximado para o calculo do erro relativo
		x_aprox = x0
		
		# Se o módulo de func'(x0) for maior que o erro, usa-se FL = func'(x0) e
		# atualiza o valor de xw
		if abs(func_derived(x0)) > eps:
			x1 = x0 - func(x0)/func_derived(x0)
			xw = x0
		# Senão, usa-se FL = func'(xw)
		else:
			x1 = x0 - func(x0)/func_derived(xw)
		
		# Valor do erro relativo
		relative_e = relative_error(x1,x_aprox)
		
		# Se o módulo de func(x1) ou o módulo da diferença entre as aproximações
		# x1 e x0 for menor que o erro, d = x1
		if abs(func(x1)) < eps or abs(x1 - x0) < eps:
			#return x1
			ans = x1
		# Caso a raiz não seja encontrada, atualiza o valor da aproximação x0
		x0 = x1
		# Adiciona dados a serem escritos
		plot_data.append((x1, relative_e))
	# Cria o arquivo a ser usado para os dados da bisseção
	File = open("Newton-Raphson", "w")
	File.close()    
	# Escreve dados no arquivo
	write_data(plot_data, "Newton-Raphson")
	# Gera plot dos dados
	generate_plot("Newton-Raphson")
	# Retorna a resposta
	return ans;
