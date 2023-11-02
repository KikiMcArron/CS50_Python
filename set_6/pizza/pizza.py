import sys
from tabulate import tabulate


def main():
	try:
		if len(sys.argv) < 2:
			sys.exit('Too few command-line arguments')
		elif len(sys.argv) > 2:
			sys.exit('Too many command-line arguments')
		elif str(sys.argv[1][-4:]) != '.csv':
			sys.exit('Not a CSV file')
		else:
			csv_to_table(sys.argv[1])
	except FileNotFoundError:
		sys.exit('File not exist')


def csv_to_table(f):
	menu = []
	with open(f, "r") as file:
		for line in file:
			item, small, large = line.rstrip().split(',')
			menu.append({'item': item, 'small': small, 'large': large})
		print(tabulate(menu[1:], menu[0], tablefmt='grid'))


if __name__ == "__main__":
	main()
