from function_box import f, f_derived

# Recebe como parâmetros o valor da aproximação inicial e a precisão
def newton_raphson(x0, eps):
	# Se o módulo de f(x0) for menor que o erro, d = x0
	if abs(f(x0)) < eps:
		return x0
	
	# Inicializa xw com o valor da aproximação inicial
	xw = x0

	# Número de iterações k vai de 1 a 999 ou até encontrar a raiz d
	for k in range(1, 1000):
		# Nova aproximação x1 é calculada a partir da função de iteração do
		# método com FL e arredonda o valor para 5 casas decimais

		# Se o módulo de f'(x0) for maior que o erro, usa-se FL = f'(x0) e
		# atualiza o valor de xw
		if abs(f_derived(x0)) > eps:
			x1 = round(x0 - f(x0)/f_derived(x0), 5)
			xw = x0
		# Senão, usa-se FL = f'(xw)
		else:
			x1 = round(x0 - f(x0)/f_derived(xw), 5)

		# Se o módulo de f(x1) ou o módulo da diferença entre as aproximações
		# x1 e x0 for menor que o erro, d = x1
		if abs(f(x1)) < eps or abs(x1 - x0) < eps:
			return x1

		# Caso a raiz não seja encontrada, atualiza o valor da aproximação x0
		x0 = x1