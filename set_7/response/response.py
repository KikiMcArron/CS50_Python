from validator_collection import validators, errors


def main():
	print(count(input("What is your email address?: ")))


def count(s):
	try:
		validators.email(s)
		return "Valid"
	except errors.InvalidEmailError:
		return "Invalid"


if __name__ == "__main__":
	main()
