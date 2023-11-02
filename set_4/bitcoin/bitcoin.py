import requests
import sys

try:
	if len(sys.argv) != 2:
		sys.exit('Missing command-line argument')

	response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
	o = response.json()
	rate = o["bpi"]["USD"]["rate_float"]
	result = rate * float(sys.argv[1])
	print(f'${result:,.4f}')
except ValueError:
	sys.exit('Command-line argument is not a number')
