import sys
from datetime import date
import inflect


def main():
	dob = birthday()
	print(f"{minutes(dob)[0].title()}{minutes(dob)[1:]} minutes")


def birthday():
	try:
		dob = date.fromisoformat(input("Date of Birth: "))
	except ValueError:
		sys.exit("Invalid date")
	return dob


def minutes(date1):
	days_from = abs(date.today() - date1)
	minutes_from = str(days_from * 1440).split(sep=" ")[0]
	engine = inflect.engine()
	minutes_text = engine.number_to_words(int(minutes_from), andword="")
	return minutes_text


if __name__ == "__main__":
	main()
