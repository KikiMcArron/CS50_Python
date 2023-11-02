def main():
	text = input("Write something -->")
	convert(text)


def convert(this):
	print(this.replace(":)", "🙂").replace(":(", "🙁"))


main()