class Node():
	"""docstring for Node"""
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList():
	"""docstring for LinkedList"""
	def __init__(self):
		self.head = None

	def print_list(self):

		if self.head is None:
			print("List has no items")
			return

		tmp = self.head
		while tmp is not None:
			print(tmp.data, end=" ")
			tmp = tmp.next
		return

	def insert_last(self, new_data):

		#check if the linked list is existed
		new_node = Node(new_data)
		if self.head is None:
			self.head = new_node
		else:	
			tmp = self.head
			while tmp.next is not None:
				tmp = tmp.next
			tmp.next = new_node
		return self.head

	def delete_first(self):
		tmp = self.head.data
		self.head = self.head.next
		self.next = None

		return tmp

	def rotate_left(self):

		d = self.delete_first()
		self.insert_last(d)

		return
if __name__ == "__main__":

	first = LinkedList()

	first.insert_last(22)
	first.insert_last(33)
	first.insert_last(44)
	first.insert_last(55)
	first.insert_last(66)
	first.insert_last(77)
	first.insert_last(88)
	first.insert_last(99)

	print(23*"=")
	print("Original Linked List")
	first.print_list()
	print("\n"+23*"=")
	
	print("New Linked List")
	first.rotate_left()
	first.print_list()
	print("\n"+23*"=")