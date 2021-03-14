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

	def insert_first(self, new_data):

		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	def delete_first(self):

		self.head = self.head.next
		self.next = None

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


	def delete_last(self):

		second_last = self.head
		while second_last.next.next is not None :
			second_last = second_last.next
		second_last.next = None

		return self.head

	def insert_node_at_position(self, data, position):

		new_node = Node(data)
		counter = 0
		tmp = self.head
		while counter < position - 1:
			counter += 1
			tmp = tmp.next
		new_node.next = tmp.next
		tmp.next = new_node
		return self.head

	def delete_node_at_position(self, position):
		if position == 0:
			self.head = self.head.next
			self.next = None

		counter = 0 
		tmp = self.head
		while counter < position - 1:
			counter += 1
			tmp = tmp.next

		tmp.next = tmp.next.next
		tmp = None
		return self.head


	def reverse_print(self, tmp):
		#using recursion
		if tmp is not None:
			self.reverse_print(tmp.next)
			print(tmp.data)
		else:
			return 

	def reverse_linked_list(self):
		prev = None
		current = self.head
		n = current
		while current is not None:
			n = current.next
			current.next = prev
			prev = current
			current = n
		self.head = prev
		return prev


	def get_length(self):

		counter = 0
		tmp = self.head
		while tmp is not None:
			counter += 1
			tmp = tmp.next
		print(counter) 

	def find_item(self, data):

		tmp = self.head
		while tmp is not None:
			if tmp.data == data:
				return True

			tmp = tmp.next
		return False
		
	def merge_lists(self, l):
		tmp = self.head.next
		while tmp is not None:
			tmp = tmp.next
		tmp = l.head
		l.head = None
		return self.head




if __name__ == "__main__":

	first = LinkedList()

	first.head = Node(1)
	second = Node(2)
	third = Node(3)
	forth = Node(4)
	fifth = Node(5)
	sixth = Node(14)
	seventh = Node(15)
	eight = Node(9)
		
	first.head.next = second
	second.next = third
	third.next = forth
	forth.next = fifth
	fifth.next = sixth
	sixth.next = seventh
	seventh.next = eight

	# l1 = LinkedList()
	# l1.head = Node(1)
	# l1_2 = Node(2)
	# l1.head.next = l1_2

	# l2 = LinkedList()
	# l2.head = Node(3)
	# l2_2 = Node(4)
	# l2.head.next = l2_2

	# print("The List is")
	first.print_list()
	print()
	# first.reverse_linked_list()
	# first.print_list()

	# l1.merge_lists(l2)
	# l1.print_list()
	# print("Reversed Print")
	# print(first.reverse_linked_list())

	# print("-----")
	# first.insert_node_at_position(1, 2)
	# first.print_list()
	# print("-----")

	first.delete_node_at_position(3)
	first.print_list()
	# first.print_list()
	# print("Insert First")
	# first.insert_first(5)
	# first.print_list()

	# print("-----")
	# print("Insert Last")
	# first.insert_last(6)
	# first.print_list()

	# print("-----")
	# print("The Length ")
	# first.get_length()

	# print("-----")
	# print("Delet First")
	# first.delete_first()
	# first.print_list()

	# print("-----")
	# print("Delete Last")
	# first.delete_last()
	# first.print_list()

	# print("----")
	# print("Search")
	# if first.find_item(2):
	# 	print("Found")
	# else:
	# 	print("Not Found")
	# first.reverse_print(first.head)
