class Queue():
	"""docstring for Queue"""
	def __init__(self, max_size):
		self.count = 0 #num of elements in the array
		self.first = 0 # the first(first elemnt) of the array
		self.last = max_size -1 # the last(last element) of the array
		self.qarray = [None] * max_size # actual array

	def is_empty(self):
		return self.count == 0

	def is_full(self):
		return self.count == len(self.qarray)
	def __str__(self):
		return ' '.join([str(i) for i in self.qarray])
	def __len__(self):
		return self.count

	def insert(self, data):
		if self.is_full():
			return Exception("Queue is Full")
		else:
			self.last = (self.last + 1) % len(self.qarray)
			self.qarray[self.last] = data
			self.count += 1

	def remove(self):
		if self.is_empty():
			return Exception("Queue is Empty")
		else:
			data = self.qarray[self.first]
			self.first = (self.first + 1) % len(self.qarray)
			self.count -= 1

			return data


if __name__ == '__main__':
	q = Queue(5)
	# q.insert(5)
	# q.insert(26)
	# q.insert(12)
	# q.insert(39)
	# q.insert(0)

	# print(q)
	# print(q.remove())
	# print(q)
	# print(q.remove())
	# print(q)
	q.insert(10)
	print(q)
	q.insert(20)
	print(q)
	q.remove()
	print(q)
	q.remove()
	print(q)
	q.insert(10)
	print(q)
	q.insert(20)
	print(q)
	q.insert(30)
	print(q)
	q.insert(40)
	print(q)
	q.insert(50)
	print(q)
	q.remove()
	print(q)
	q.insert(60)
	print(q)