import sys
import pyfiglet

if len(sys.argv) == 1:
	text = input('Input: ')
	pyfiglet.print_figlet(text)
elif len(sys.argv) == 3:
	if sys.argv[1] == '-f' or sys.argv[1] == '--font':
		try:
			pyfiglet.print_figlet('', font=sys.argv[2])
			text = input('Input: ')
			pyfiglet.print_figlet(text, font=sys.argv[2])
		except pyfiglet.FontNotFound:
			print(f'{sys.argv[2]} is not a font')
			sys.exit(1)
	else:
		print('Wrong args')
		sys.exit(1)
else:
	print('Too few args')
	sys.exit(1)
