import fuel
import pytest


def test_convert():
	with pytest.raises(ValueError):
		fuel.convert('2/1')
	with pytest.raises(ZeroDivisionError):
		fuel.convert('2/0')
	assert fuel.convert('2/3') == 67


def test_gauge():
	assert fuel.gauge(67) == '67%'
	assert fuel.gauge(0) == 'E'
	assert fuel.gauge(1) == 'E'
	assert fuel.gauge(100) == 'F'
	assert fuel.gauge(99) == 'F'
