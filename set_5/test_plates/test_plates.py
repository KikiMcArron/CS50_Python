import plates


def test_valid_alphabet_begin():
	assert plates.is_valid("1250") == False


def test_zero_in_place():
	assert plates.is_valid("CS050") == False


def test_proper_length():
	assert plates.is_valid("CS503725") == False


def test_numbers_rules():
	assert plates.is_valid("CS5N0") == False


def test_no_punctuation():
	assert plates.is_valid("CS5:0") == False
