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

	def __len__(self):
		return self.count

	def enqueue(self, data):
		if self.is_full():
			return Exception("Queue is Full")
		else:
			self.last = (self.last + 1) % len(self.qarray)
			self.qarray[self.last] = data
			self.count += 1

	def dqueue(self):
		if self.is_empty():
			return Exception("Queue is Empty")
		else:
			data = self.qarray[self.first]
			self.first = (self.first + 1) % len(self.qarray)
			self.count -= 1
			return data


if __name__ == '__main__':
	q = Queue(5)
	for i in range(0,5):
		q.enqueue(i)

	print(len(q))
	print(q.is_empty())

	for i in range(len(q)):
		print(q.dqueue())