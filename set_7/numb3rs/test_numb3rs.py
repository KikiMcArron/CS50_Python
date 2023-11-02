from numb3rs import validate


def test1_numb3rs():
	assert validate('1.1.1.1') == True


def test2_numb3rs():
	assert validate("255.255.255.255") == True


def test3_numb3rs():
	assert validate("255.123.149.1") == True


def test4_numb3rs():
	assert validate("256.123.149.1") == False


def test5_numb3rs():
	assert validate("256,123.149.1") == False


def test6_numb3rs():
	assert validate("wrong ip") == False


def test7_numb3rs():
	assert validate("255.400.0.1") == False
