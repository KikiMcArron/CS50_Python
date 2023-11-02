from bank import value


def test_hello():
	assert value("hello") == 0


def test_h():
	assert value("holly") == 20


def test_else():
	assert value("koko") == 100


def test_nocaseint():
	assert value("Hoko") == 20
