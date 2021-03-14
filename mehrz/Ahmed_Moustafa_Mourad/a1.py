class Node():
	"""docstring for Node"""
	def __init__(self, name, age, degree):
		self.name = name
		self.age = age
		self.degree = degree 
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
			print(tmp.name, tmp.age, tmp.degree)
			tmp = tmp.next
		return

	def insert_last(self, name, age, degree):

		#check if the linked list is existed
		new_node = Node(name, age, degree)
		if self.head is None:
			self.head = new_node
		else:	
			tmp = self.head
			while tmp.next is not None:
				tmp = tmp.next
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

if __name__ == "__main__":

	first = LinkedList()
	passed = LinkedList()

	print(30*"=")
	print("All Students")
	print(30*"=")
	first.head = Node("snow", 21, 43)
	first.insert_last("m1m0n", 15, 95)
	first.insert_last("test", 15, 40)
	first.insert_last("admin", 16, 20)
	first.insert_last("mysql", 18, 89)
	first.insert_last("guest", 16, 45)
	first.insert_last("user", 15, 40)
	first.insert_last("oracle", 15, 90)
	first.insert_last("ctf", 15, 99)
	first.insert_last("ansible", 15, 0)
	first.insert_last("puppet", 15, 35)
	first.print_list()
	print(30*"=")

	tmp = first.head
	pos = 0
	while tmp is not None:
		if tmp.degree >= 50:
			passed.insert_last(tmp.name, tmp.age, tmp.degree)
			first.delete_node_at_position(pos)
			pos -= 1
		tmp = tmp.next
		pos += 1

	print("Passed Students (degree >= 50)")
	print(30*"=")
	passed.print_list()

	print(30*"=")
	print("Faild Students (degree < 50)")
	print(30*"=")
	first.print_list()
