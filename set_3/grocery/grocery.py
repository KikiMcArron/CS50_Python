def main():
	shopping_list = {}
	create_list(shopping_list)
	print_list(shopping_list)


def create_list(elements_list):
	while True:
		try:
			item = input()
			if item in elements_list:
				elements_list[item] += 1
			else:
				elements_list[item] = 1
		except EOFError:
			break


def print_list(elements_list):
	for element in sorted(elements_list):
		print(elements_list[element], element.upper())


main()
