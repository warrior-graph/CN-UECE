from function_box import f
from error_box import relative_error

# Recebe como parâmetro os valores das aproximações iniciais e a precisão
def secant(x0, x1, eps, func=f):
	# Se o módulo de f(x0) for menor que o erro, d = x0
	if abs(func(x0)) < eps:
		return x0

	# Se o módulo de f(x1) ou o módulo da diferença entre as aproximações x1 e
	# x0 for menor que o erro, d = x1
	if abs(func(x1)) < eps or abs(x1 - x0) < eps:
		return x1

	# Número de iterações k vai de 1 a 1000 ou até encontrar a raiz d
	for k in range(1, 1001):
		# Nova aproximação x2 é calculada a partir da função de iteração do
		# método
		x2 = x1 - func(x1) / (func(x1) - func(x0)) * (x1 - x0)

		# Se o módulo de f(x2) ou o módulo da diferença entre as aproximações
		# x2 e x1 for menor que o erro, d = x2
		if abs(func(x2)) < eps or abs(x2 - x1) < eps:
			return x2
		
		# Valor aproximado para o calculo do erro relativo
		x_aprox = x1
		# Calcula o erro relativo 
		relative_e = relative_error(x_aprox,x2)
		
		# Caso raiz não seja encontrada, atualiza os valores das aproximações
		x0 = x1
		x1 = x2
