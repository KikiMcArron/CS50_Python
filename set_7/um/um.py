import re


def main():
	print(count(input("Input: ")))


def count(s):
	ums = re.findall(r'\b[u|U]m\b', s)
	return len(ums)


if __name__ == "__main__":
	main()
