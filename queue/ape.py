class Node():
	"""docstring for Node"""
	def __init__(self, data):
		self.data = data
		self.next = None


class Queue():
	"""docstring for Queue"""
	def __init__(self):
		self.head =  None
		self.size = 0

	def is_empty(self):
		return self.head == None

	def enqueue(self, data):
		# Insert last
		new_node = Node(data)
		tmp = self.head
		while tmp is not None:
			tmp = tmp.next
		new_node.next = new_node


	def print_list(self):
		if self.head is None:
			print("List has no items")
			return

		tmp = self.head
		while tmp is not None:
			print(tmp.data)
			tmp = tmp.next
		return




if __name__ == '__main__':
	
	first = Queue()

	first.head = Node(1)
	second = Node(2)
	third = Node(3)
	forth = Node(4)
	fifth = Node(5)


	first.head.next = second
	second.next = third
	third.next = forth
	forth.next = fifth


	first.print_list()