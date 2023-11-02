from fpdf import FPDF


def main():
	# Getting name
	disp_name = input('Name: ')

	# Setting pdf page properties
	pdf = FPDF()
	pdf.add_page()
	pdf.set_font('helvetica', 'B', 36)

	# Adding head text centered horizontal
	head = 'CS50 Shirtificate'
	head_width = pdf.get_string_width(head)
	head_x = (pdf.w - head_width) / 2
	pdf.text(head_x, 30, head)

	# Adding shirt image
	pdf.image('shirtificate.png', x=10, y=50, w=190)

	# Adding personalized text on t-shirt
	pdf.set_font('helvetica', 'B', 25)
	text = f'{disp_name} took CS50'
	text_width = pdf.get_string_width(text)
	text_x = (pdf.w - text_width) / 2
	pdf.set_text_color(255, 255, 255)
	pdf.text(text_x, 115, text)

	# Returning final pdf file
	pdf.output('shirtificate.pdf')


if __name__ == "__main__":
	main()
