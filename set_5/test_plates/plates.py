def main():
	string = input("Plate: ")
	if is_valid(string):
		print("Valid")
	else:
		print("Invalid")


def is_valid(string):
	if start_with_letters(string) and proper_length(string) and numbers_rules(string) and no_punctuation(string):
		return True
	else:
		return False


def start_with_letters(string):
	if string[0:2].isalpha():
		return True
	else:
		return False


def proper_length(string):
	if 1 < len(string) < 7:
		return True
	else:
		return False


def numbers_rules(string):
	end_str = string[2:]
	if end_str[0] == "0":
		return False
	elif len(end_str) == 0 or end_str.isdigit():
		return True
	elif end_str[0] != "0":
		for i in range(len(end_str) - 1):
			if end_str[i].isdigit():
				if end_str[i + 1:].isdigit():
					return True
				else:
					return False
			else:
				return True
	else:
		return False


def no_punctuation(string):
	for i in string:
		if i.isalpha() or i.isdigit():
			return True
		else:
			return False


if __name__ == "__main__":
	main()
