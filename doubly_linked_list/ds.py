class Node:

	def __init__(self, data=None):
		self.data = data
		self.next = None
		self.prev = None

class DoublyLinkedList:
	def __init__(self):
		self.head = None

	def print_list(self):
		tmp = self.head 
		while tmp is not None : 
			print(tmp.data, end=" ") 
			tmp = tmp.next 	

	def insert_first(self, new_data):

		new_node = Node(new_data)
		new_node.next = self.head
		if self.head is not None:
			self.head.prev = new_node

		self.head = new_node

	def reverse_print(self, tmp):
		# Using Recursion
		if tmp is not None :
			self.reverse_print(tmp.next)
			print(tmp.data, end=" ")
		else:
			return

	def reverse(self):
		temp = None
		current = self.head
		while current is not None:
			temp = current.prev
			current.prev = current.next
			current.next = temp
			current = current.prev

		if temp is not None:
			self.head = temp.prev

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
	

	def sorted_insert1(self, data):
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

def sorted_insert2(head, new_node): 

	current = None
	if head is None: 
		head = new_node 

	elif head.data >= new_node.data : 
		new_node.next = head 
		new_node.next.prev = new_node 
		head = new_node 
	else : 
		current = head 
		while current.next is not None and current.next.data < new_node.data: 
			current = current.next

		new_node.next = current.next

		if current.next is not None: 
			new_node.next.prev = new_node 

		current.next = new_node 
		new_node.prev = current 
	
	return head
	
def insertion_sort(head):  
	sort = None
	current = head
	while current is not None : 
		n = current.next
		current.prev = current.next = None
		sort = sorted_insert2(sort, current) 
		current = n
	head = sort
	return head

if __name__ == '__main__':
	
	first = DoublyLinkedList()
	first.insert_first(15)
	first.insert_first(22)
	first.insert_first(130)
	first.insert_first(66)
	first.insert_first(55)
	first.insert_first(44)
	first.insert_first(35)

	print(43*"=")
	print("Original Double Linked List")
	first.print_list()
	print()

	print(43*"=")
	print("Reversed Double Linked List")
	first.reverse()
	first.print_list()
	print()

	print(43*"=")
	print("Reversed Double Linked List Using Recursion")
	first.reverse_print(first.head)
	print()

	print(43*"=")
	print("Sorted Double Linked List ( V1 )")
	insertion_sort(first.head)
	first.print_list()	
	print()
	print(43*"=")

	print("Sorted Double Linked List ( V2 )")

	new_node = DoublyLinkedList()
	new_node.head = Node(0)
	tmp = first.head

	while tmp is not None:
		new_node.sorted_insert1(tmp.data)
		tmp = tmp.next
	
	new_node.print_list()
	print()
	print(43*"=")
'''
===========================================
Original Double Linked List
35 44 55 66 130 22 15 
===========================================
Reversed Double Linked List
15 22 130 66 55 44 35 
===========================================
Reversed Double Linked List Using Recursion
35 44 55 66 130 22 15 
===========================================
Sorted Double Linked List ( V1 )
15 22 35 44 55 66 130 
===========================================
Sorted Double Linked List ( V2 )
0 15 22 35 44 55 66 130 
===========================================
'''
