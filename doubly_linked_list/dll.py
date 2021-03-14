class Node():
	"""docstring for Node"""
	def __init__(self,data):
		self.next = None
		self.prev = None
		self.tail = None
		self.data = data
		
class DoublyLinkedList():
	"""docstring for DoublyLinkedList"""
	def __init__(self):
		self.head = None
		self.tail = None
		
	def print_list(self):
		if self.head is None:
			print("No Items")

		tmp = self.head
		while tmp is not None:
			print(tmp.data)
			tmp = tmp.next
		return


	def insert_first(self, new_data):

		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node
		new_node.prev = None

	def insert_last(self, new_data):

		new_node = Node(new_data)
		tmp = self.head
		while tmp.next is not None:
			tmp = tmp.next
		tmp.next = new_node
		new_node.next = None

	def reverse(self, tmp):
		# Using Recursion
		if tmp is not None :
			self.reverse(tmp.next)
			print(tmp.data)
		else:
			return

	def insert_at_position(self, data, position):
		new_node = Node(data)
		counter = 0
		tmp = self.head
		while counter < position - 1:
			counter += 1
			tmp = tmp.next

		new_node.next = tmp.next
		tmp.next = new_node
		new_node.prev = tmp
		tmp.next.prev = new_node	
		return self.head
	

	def sorted_insert(self, data):
		pos = 0
		tmp = self.head
		while tmp is not None:
			if data <= tmp.data:
				break
			else:
				pos += 1
				tmp = tmp.next
		self.insert_at_position(data, pos)
		return self.head


	# def rev(self):
	# 	while self.head is not None:
	# 		self.head.next, self.head.prev , self.head = self.head.prev, self.head.next, self.head.next			

	# 	# self.head.next, self.head.prev = self.head.prev, None
	# 	self.head.next = self.head.prev
	# 	self.head.prev = None

	# 	return self.head

	def rev(self):
		temp = None
		current = self.head
		while current is not None:
			temp = current.prev
			current.prev = current.next
			current.next = temp
			current = current.prev
		if temp is not None:
			self.head = temp.prev


if __name__ == "__main__":
	
	first = DoublyLinkedList()
	first.head = Node(15)
	first.insert_first(22)
	first.insert_last(3)
	first.insert_last(66)
	first.insert_last(55)
	first.insert_last(44)
	first.print_list()

	print(10*"-")
	print("Reverse DLL")
	# first.reverse(first.head)
	first.rev()
	first.print_list()

	print(10*"-")
	# new_node = DoublyLinkedList()
	# new_node.head = Node(first.head.data)
	# tmp = first.head

	# while tmp is not None:
	# 	new_node.sorted_insert(tmp.data)
	# 	tmp = tmp.next
	
	# new_node.print_list()
