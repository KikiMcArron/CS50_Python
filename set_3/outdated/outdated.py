def main():
	months = [
		"January",
		"February",
		"March",
		"April",
		"May",
		"June",
		"July",
		"August",
		"September",
		"October",
		"November",
		"December"
	]

	new_date(months)


def new_date(mon):
	while True:
		try:
			date = input("Date: ")
			if date.split(' ')[0] in mon:
				m = mon.index(date.split(' ')[0]) + 1
				d = date.split(' ')[1]
				y = int(date.split(' ')[2])
				if d[-1] == ',' and int(d.strip(',')) in list(range(0, 32)) and y in list(range(0, 10000)):
					d = int(d.strip(','))
					print(f"{y}-{m:02}-{d:02}")
					break
			elif int(date.split('/')[0]) in list(range(1, 13)):
				m = int(date.split('/')[0])
				d = int(date.split('/')[1])
				y = int(date.split('/')[2])
				if d in list(range(0, 32)) and y in list(range(0, 10000)):
					print(f"{y}-{m:02}-{d:02}")
					break
		except ValueError:
			pass


main()
