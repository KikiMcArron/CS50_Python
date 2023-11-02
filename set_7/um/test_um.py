from um import count


def test1_um():
	assert count('Um?') == 1


def test2_um():
	assert count('Um.. yes um trum bum um') == 3


def test3_um():
	assert count('um.. yes um trum bum um') == 3
