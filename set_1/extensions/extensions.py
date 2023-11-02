def main():
	file_name = input('File name: ').lower().strip()
	file_type(file_name)


def file_type(ext):
	extension = (ext.rpartition('.'))[2]
	match extension:
		case 'gif' | 'jpeg' | 'png':
			print('image/' + extension)
		case 'jpg':
			print('image/jpeg')
		case 'txt':
			print('text/plain')
		case 'pdf' | 'zip':
			print('application/' + extension)
		case _:
			print('application/octet-stream')


main()
