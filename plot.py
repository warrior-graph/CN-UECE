import numpy as np
import matplotlib.pyplot as plt
import matplotlib.axes as ax
import sys

def generate_plot():
	file_name = input("Enter a method name: \n")
	data = np.genfromtxt(file_name, skip_header = 0, skip_footer = 0, names = True, dtype = 'float', delimiter = ' ')
	x = []
	y = []
	plt.xlabel('D Value')
	plt.ylabel('Relative Error')
	#plt.title(file_name)
	for i in data:
		x.append(i[0])
		y.append(i[1])

	plt.plot(x, y, color = 'black', label = file_name)
	plt.legend()
	plt.show()
generate_plot()
