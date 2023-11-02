def main():
	price = 50
	count(price)


def count(p):
	while p > 0:
		print('Amount Due: ', p)
		coin = int(input('Insert Coin: '))
		if coin == 25 or coin == 10 or coin == 5:
			p = p - coin
	print('Change Owed: ', -p)


main()
