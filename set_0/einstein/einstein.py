def main():
	m = input("What is the mass? ")
	energy(int(m))


def energy(mass):
	qc = 300000000 ** 2
	print(f"Energy = {mass * qc}N")


main()
