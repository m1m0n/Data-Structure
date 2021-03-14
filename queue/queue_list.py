class Queue():
	"""docstring for Queue"""
	def __init__(self):
		self.qlist = list()

	def is_empty(self):
		return len(self) == 0

	def __len__(self):
		return len(self.qlist)

	def enqueue(self, data):
		self.qlist.append(data)

	def dqueue(self):
		if self.is_empty():
			return Exception("Quesue is Empty")
		else:
			return self.qlist.pop(0)

		
if __name__ == '__main__':
	q = Queue()
	q.enqueue(28)
	q.enqueue(19)
	q.enqueue(45)
	print(len(q))

	print(q.dqueue())
	print(q.dqueue())
	print(q.dqueue())
	print(q.dqueue())