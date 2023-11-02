import inflect


def main():
	names = add_names()
	sentence = 'Adieu, adieu, to'
	print_sent(names, sentence)


def add_names():
	n = []
	while True:
		try:
			name = input('Name: ')
			n.append(name)
		except EOFError:
			break
	return n


def print_sent(n, s):
	inf = inflect.engine()
	print(s + ' ' + inf.join(n))


main()
