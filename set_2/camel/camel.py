# Simple program to convert CamelCase input into SnakeCase

def main():
	camel = input('camelCase: ')
	to_snake(camel)


def to_snake(sentence):
	print('snake_case: ', end="")
	for char in sentence:
		if char.isupper():
			print('_' + char.lower(), end="")
		else:
			print(char, end="")


main()
