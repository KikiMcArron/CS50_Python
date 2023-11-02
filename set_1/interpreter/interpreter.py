def main():
	expression = input('Expression: ')
	interpreter(expression)


def interpreter(exp):
	x = float(exp.split(' ')[0])
	y = exp.split(' ')[1]
	z = float(exp.split(' ')[2])
	if y == '+':
		print(round(x + z, 1))
	elif y == '-':
		print(round(x - z, 1))
	elif y == '*':
		print(round(x * z, 1))
	else:
		print(round(x / z, 1))


main()
