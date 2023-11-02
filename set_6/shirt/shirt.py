import sys
from PIL import Image, ImageOps


def main():
	try:
		if len(sys.argv) < 3:
			sys.exit('Too few command-line arguments')
		elif len(sys.argv) > 3:
			sys.exit('Too many command-line arguments')
		elif str(sys.argv[1][-4:]) != str(sys.argv[2][-4:]):
			sys.exit('Input and output have different extensions')
		else:
			pic_manipulate(sys.argv[1], sys.argv[2])
	except FileNotFoundError:
		sys.exit('File not exist')


def pic_manipulate(before, after):
	shirt = Image.open("shirt.png")
	pic = Image.open(before)
	pic_fit = ImageOps.fit(pic, shirt.size)
	pic_fit.paste(shirt, (0, 0), shirt.split()[3])
	pic_fit.save(after)


if __name__ == "__main__":
	main()
