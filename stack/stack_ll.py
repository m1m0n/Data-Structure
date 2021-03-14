class Node():
	"""docstring for Node"""
	def __init__(self, data):
		self.data = data
		self.next = None

class Stack():
	def __init__(self):
		self.head = None
		self.size = 0

	def __str__(self):
		current = self.head
		out = ""
		while current is not None:
			out += str(current.data) + " -> "
			current = current.next
			# print(out)

		return out[:-3]

	def get_size(self):
		return self.size

	def is_empty(self):
		return self.size == 0

	def make_empty(self):
		if self.size > 0:
			self.size = 0
		return

	def peek(self):
		if self.is_empty():
			raise Exception("Peeking from an empty Stack")
		return self.head.next.data


	def push(self, data):	
		# Insert first function from linked list
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node
		self.size += 1

	def pop(self):
		# Delete first function from linked linked
		tmp = self.head
		self.head = self.head.next
		tmp.next = None
		self.size -= 1
		return tmp.data

	def sum(self):
		tmp = self.head
		s = 0
		while tmp is not None:
			s += int(tmp.data)
			tmp = tmp.next

		return s
if __name__ == "__main__":

	stack = Stack()
	stack.push(1)
	print(stack)
	stack.push(2)
	print(stack)
	stack.push(3)
	print(stack)
	print(stack.sum())
	# print(stack.pop())
	# print(stack)
	# for i in range(1,11):
	# 	stack.push(i)
	# print(stack.get_size())
	# print(stack)

	# for _ in range(1,6):
	# 	remove = stack.pop()
	# 	print("Pop : " + str(remove))
	# print(stack)
	# print(stack.get_size())
	# stack.make_empty()
	# print(stack)