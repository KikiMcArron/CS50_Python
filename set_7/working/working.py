import re


def main():
	print(convert(input("Hours: ").strip()))


def convert(s):
	pm_pattern = {
		'1': '13',
		'2': '14',
		'3': '15',
		'4': '16',
		'5': '17',
		'6': '18',
		'7': '19',
		'8': '20',
		'9': '21',
		'10': '22',
		'11': '23',
		'12': '12'
		}
	am_pattern = {
		'1': '01',
		'2': '02',
		'3': '03',
		'4': '04',
		'5': '05',
		'6': '06',
		'7': '07',
		'8': '08',
		'9': '09',
		'10': '10',
		'11': '11',
		'12': '00'
		}
	pattern = r'^(1[0-2]|[1-9])(:[0-5][0-9])? [A|P]M to (1[0-2]|[1-9])(:[0-5][0-9])? [A|P]M$'
	match = re.match(pattern, s)
	if not match:
		raise ValueError
	else:
		start, end = s.split(" to ")
		if "AM" in start:
			conv_start = am_pattern[match.group(1)]
		else:
			conv_start = pm_pattern[match.group(1)]
		if not match.group(2):
			start_mins = ':00'
		else:
			start_mins = match.group(2)
		if "AM" in end:
			conv_end = am_pattern[match.group(3)]
		else:
			conv_end = pm_pattern[match.group(3)]
		if not match.group(4):
			end_mins = ':00'
		else:
			end_mins = match.group(4)
		return f'{conv_start}{start_mins} to {conv_end}{end_mins}'


if __name__ == "__main__":
	main()
