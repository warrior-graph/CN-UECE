import random
from function_box import f

# Recebe como parâmetro os valores das aproximações iniciais e a precisão
def secant(x0, x1, eps):
	# Se o módulo de f(x0) for menor que o erro, d = x0
	if abs(f(x0)) < eps:
		return x0

	# Se o módulo de f(x1) ou o módulo da diferença entre as aproximações x1 e
	# x0 for menor que o erro, d = x1
	if abs(f(x1)) < eps or abs(x1 - x0) < eps:
		return x1

	# Número de iterações k vai de 1 a 1000 ou até encontrar a raiz d
	for k in range(1, 1001):
		# Nova aproximação x2 é calculada a partir da função de iteração do
		# método e arredonda o valor para 5 casas decimais
		x2 = round(x1 - f(x1) / (f(x1) - f(x0)) * (x1 - x0), 5)

		# Se o módulo de f(x2) ou o módulo da diferença entre as aproximações
		# x2 e x1 for menor que o erro, d = x2
		if abs(f(x2)) < eps or abs(x2 - x1) < eps:
			return x2
	
		# Caso raiz não seja encontrada, atualiza os valores das aproximações
		x0 = x1
		x1 = x2