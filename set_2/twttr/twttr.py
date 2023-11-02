def main():
	twit = input('Input: ')
	shorten(twit)


def shorten(string):
	vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
	for i in vowels:
		string = string.replace(i, '')
	return string


if __name__ == "__main__":
	main()
