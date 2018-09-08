from function_box import f, f_derived

# Recebe como parâmetros os valores do intervalo (a, b) e a precisão
def newton_raphson(a, b, eps, func=f, func_derived=f_derived):
	# Utiliza como aproximação inicial a média entre os valores do intervalo
	x0 = (a + b) / 2
	# Se o módulo de f(x0) for menor que o erro, d = x0
	if abs(func(x0)) < eps:
		return x0
	
	# Inicializa xw com o valor da aproximação inicial
	xw = x0

	# Número de iterações k vai de 1 a 1000 ou até encontrar a raiz d
	for k in range(1, 1001):
		# Nova aproximação x1 é calculada a partir da função de iteração do
		# método com FL

		# Se o módulo de func'(x0) for maior que o erro, usa-se FL = func'(x0) e
		# atualiza o valor de xw
		if abs(func_derived(x0)) > eps:
			x1 = x0 - func(x0)/func_derived(x0)
			xw = x0
		# Senão, usa-se FL = func'(xw)
		else:
			x1 = x0 - func(x0)/func_derived(xw)

		# Se o módulo de func(x1) ou o módulo da diferença entre as aproximações
		# x1 e x0 for menor que o erro, d = x1
		if abs(func(x1)) < eps or abs(x1 - x0) < eps:
			return x1

		# Caso a raiz não seja encontrada, atualiza o valor da aproximação x0
		x0 = x1
