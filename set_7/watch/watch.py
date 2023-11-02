import re


def main():
	print(parse(input("HTML: ").strip()))


def parse(s):
	if not "embed/" in s:
		return None
	elif not "iframe" in s:
		return None
	else:
		movie_id = re.sub(r'^.*src=\"(https?)?://(www\.)?youtube\.com/embed/', '', s)
		movie_id = re.sub(r'\".*$', '', movie_id)
		return f'https://youtu.be/{movie_id}'


if __name__ == "__main__":
	main()
