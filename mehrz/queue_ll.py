class Node():
	"""docstring for Node"""
	def __init__(self, data):
		self.data = data
		self.next = None


class Queue():
	"""docstring for Queue"""
	def __init__(self):
		self.front = self.back = None
		self.size = 0

	def is_empty(self):
		return self.front == None

	def enqueue(self, data):
		# Insert last
		new_node = Node(data)

		if self.back == None: # ll is empty 
			self.front = self.back = new_node
			self.size += 1
			return
		else:
			self.back.next = new_node
			self.back = new_node
			self.size += 1

	def dqueue(self):
		#Remove first
		if self.is_empty():
			return
		tmp = self.front
		self.front = tmp.next
		self.size -= 1

		if self.front == None:
			self.back = None
			self.size -= 1
		return tmp.data

	def len(self):
		return self.size

if __name__ == '__main__':
	q = Queue()
	q.enqueue(10)
	q.enqueue(20)
	q.enqueue(30)
	print(q.front.data)
	print(q.back.data)
	print(q.len())
	print(q.dqueue())

	print(q.front.data)
	print(q.back.data)	
	print(q.len())