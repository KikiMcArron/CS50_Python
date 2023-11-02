def main():
	while True:
		try:
			fraction = input("Fraction: ")
			percentage = convert(fraction)
			print(gauge(percentage))
		except (ZeroDivisionError, ValueError):
			continue
		else:
			break


def convert(fraction):
	num = int(fraction.split('/')[0])
	denum = int(fraction.split('/')[1])
	output = round(num / denum * 100)
	if output > 100:
		raise ValueError
	else:
		return output


def gauge(percentage):
	if percentage <= 1:
		return 'E'
	elif percentage >= 99:
		return 'F'
	else:
		return f"{percentage}%"


if __name__ == "__main__":
	main()
