import pytest
from working import convert


def test1_working():
	assert convert('10:00 PM to 5:30 AM') == '22:00 to 05:30'


def test2_working():
	assert convert('8 AM to 5 PM') == '08:00 to 17:00'


def test3_working():
	assert convert('10:50 PM to 5:30 AM') == '22:50 to 05:30'


def test4_working():
	with pytest.raises(ValueError):
		convert('10:00 PM5:30 AM')


def test5_working():
	with pytest.raises(ValueError):
		convert('10:00 PM to 5:60 AM')
