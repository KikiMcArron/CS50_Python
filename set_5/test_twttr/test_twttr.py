from twttr import shorten


def test_shorten():
	assert shorten("krbt") == "krbt"
	assert shorten("kOlAbIrUtEk") == "klbrtk"
	assert shorten("tarotubire") == "trtbr"
	assert shorten("123") == "123"
	assert shorten("K.T,") == "K.T,"
