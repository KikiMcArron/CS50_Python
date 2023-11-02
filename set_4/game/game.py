import random
import sys


def main():
	level = get_positive_integer('Level: ')
	rdm = get_random(level)
	result(rdm)


def get_positive_integer(prompt):
	while True:
		try:
			v = int(input(prompt))
			if v <= 0:
				raise ValueError
		except ValueError:
			pass
		else:
			return v


def get_random(positive_int):
	return random.randint(1, positive_int)


def result(r):
	while True:
		try:
			g = get_positive_integer('Guess: ')
			if g < r:
				print('Too small!')
				raise ValueError
			elif g > r:
				print('Too large!')
				raise ValueError
			else:
				sys.exit('Just right!')
		except ValueError:
			pass


main()
