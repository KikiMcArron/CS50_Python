def main():
	time = input('What time is it? ')
	if 7 <= convert(time) <= 8:
		print('breakfast time')
	elif 12 <= convert(time) <= 13:
		print('lunch time')
	elif 18 <= convert(time) <= 19:
		print('dinner time')
	else:
		print('fasting time')


def convert(t):
	x = float(t.split(':')[0])
	y = float(t.split(':')[1])
	return x + y / 60


if __name__ == "__main__":
	main()
