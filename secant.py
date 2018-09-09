from function_box import f

# Recebe como parâmetro os valores das aproximações iniciais e a precisão
def secant(d0, d1, eps, func=f):
	# Inicializa a lista onde serão salvas as aproximações de d
	iter_values = []

	# Se o módulo de f(x0) for menor que o erro, d = x0
	if abs(func(d0)) < eps:
		iter_values.append(d0)
		return iter_values

	# Se o módulo de f(x1) ou o módulo da diferença entre as aproximações x1 e
	# x0 for menor que o erro, d = x1
	if abs(func(d1)) < eps or abs(d1 - d0) < eps:
		iter_values.append(d1)
		return iter_values

	# Número de iterações k vai de 1 a 1000 ou até encontrar a raiz d
	for k in range(1, 1001):
		# Nova aproximação x2 é calculada a partir da função de iteração do
		# método
		d2 = d1 - func(d1) / (func(d1) - func(d0)) * (d1 - d0)
		iter_values.append(d2)

		# Se o módulo de f(x2) ou o módulo da diferença entre as aproximações
		# x2 e x1 for menor que o erro, d = x2
		if abs(func(d2)) < eps or abs(d2 - d1) < eps:
			return iter_values
		
		# Caso raiz não seja encontrada, atualiza os valores das aproximações
		d0 = d1
		d1 = d2
