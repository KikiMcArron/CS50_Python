import sys
import csv


def main():
	try:
		if len(sys.argv) < 3:
			sys.exit('Too few command-line arguments')
		elif len(sys.argv) > 3:
			sys.exit('Too many command-line arguments')
		elif str(sys.argv[2][-4:]) != '.csv':
			sys.exit('Could not read invalid_file.csv')
		else:
			clean_csv(sys.argv[1], sys.argv[2])
	except FileNotFoundError:
		sys.exit('File not exist')


def clean_csv(f1, f2):
	students = []
	with open(f1) as file:
		reader = csv.DictReader(file)
		for row in reader:
			students.append({"name": row["name"], "house": row["house"]})
	with open(f2, "w") as file:
		writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
		writer.writeheader()
		for student in students:
			writer.writerow({
				"first": student["name"].split(",")[1].lstrip(), "last": student["name"].split(",")[0], "house": student["house"]
			})


if __name__ == "__main__":
	main()
