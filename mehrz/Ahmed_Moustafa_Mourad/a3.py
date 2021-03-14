class Queue():
	"""docstring for Queue"""
	def __init__(self, max_size):
		self.count = 0 #num of elements in the array
		self.first = 0 # the first(first elemnt) of the array
		self.last = max_size -1
		self.qarray = [0] * max_size # actual array

	def __len__(self):
		return self.count
	
	def __str__(self):
		return ' '.join([str(i) for i in self.qarray])

	def is_empty(self):
		return self.count == 0

	def is_full(self):
		return self.count == len(self.qarray)
	
	def find_max(self):
		return max(self.qarray)
	
	def get_index(self, key):
		found = 0
		for i in range(len(self.qarray)):
			if key > self.qarray[i]:
				pass
			else:
				found = i
				break
		return found

	def enqueue(self, data):
		if self.is_full():
			return Exception("Queue is Full")
		else:	
			indx = self.get_index(data)
			self.qarray.insert(indx, data)
			# self.last = (self.last + 1) % len(self.qarray)
			# self.qarray[indx] = data
			self.count += 1

	def remove(self):
		if self.is_empty():
			return Exception("Queue is Empty")
		else:
			indx = self.qarray.index(self.find_max())
			tmp = self.find_max()
			self.first = (self.first + 1) % len(self.qarray)
			self.count -= 1
			self.qarray[indx] = 0
			return tmp


if __name__ == '__main__':
	q = Queue(5)

	q.enqueue(12)
	print(q)
	q.enqueue(20)
	print(q)
	q.enqueue(10)
	print(q)
	# q.remove()
	# print(q)
	q.enqueue(39)
	print(q)
	# q.remove()
	# print(q)
	q.enqueue(16)

	print("Original Queue")
	print(q)

	print(14*"=")
	print(q.remove())
	print(q)

	print(14*"=")
	print(q.remove())
	print(q)
	print(14*"=")
	q.enqueue(15)
	print(q)
	print(q.remove())