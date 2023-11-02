# Program to count effective code lines (without empty lines)
# To run type in Terminal: "python lines.py <path\script.py>"

import sys


def main():
	try:
		if len(sys.argv) < 2:
			sys.exit('Too few command-line arguments')
		elif len(sys.argv) > 2:
			sys.exit('Too many command-line arguments')
		elif str(sys.argv[1][-3:]) != '.py':
			sys.exit('Not a Python file')
		else:
			lines_count(sys.argv[1])
	except FileNotFoundError:
		sys.exit('File not exist')


def lines_count(f):
	lines_number = 0
	with open(f, "r") as file:
		lines = file.readlines()
	for line in lines:
		if line.strip() != '' and line.lstrip()[0] != '#':
			lines_number += 1
	print(lines_number)


main()
