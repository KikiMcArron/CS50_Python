class Jar:
	def __init__(self, capacity=12, size=0):
		self.capacity = capacity
		self.size = size

	def __str__(self):
		return self.size * "🍪"

	def deposit(self, n):
		if n + self.size > self.capacity:
			raise ValueError("To many cookies in the jar!")
		else:
			self.size += n

	def withdraw(self, n):
		if self.size - n < 0:
			raise ValueError("Not enough cookies in the jar!")
		else:
			self.size -= n

	@property
	def capacity(self):
		return self._capacity

	@capacity.setter
	def capacity(self, capacity):
		if capacity < 0 or capacity != int(capacity):
			raise ValueError('Capacity is not positive integer!')
		self._capacity = capacity

	@property
	def size(self):
		return self._size

	@size.setter
	def size(self, size):
		if size < 0 or size != int(size):
			raise ValueError('Size is not positive integer!')
		self._size = size
