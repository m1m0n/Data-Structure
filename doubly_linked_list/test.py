# Python3 implementation for insertion Sort 
# on a doubly linked list 

# Node of a doubly linked list 
class Node: 
	
	def __init__(self, data): 
		self.data = data 
		self.prev = None
		self.next = None

# function to create and return a new node 
# of a doubly linked list 
def getNode(data): 

	# allocate node 
	new_node = Node(0) 

	# put in the data 
	new_node.data = data 
	new_node.prev = new_node.next = None
	return new_node 

def sorted_insert(head, new_node): 

	current = None
	if head == None: 
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
	
	return head; 
	
def insertion_sort(head):  
	sort = None
	current = head
	while current is not None : 
		n = current.next
		current.prev = current.next = None
		sort = sorted_insert(sort, current) 
		current = n
	head = sort
	return head 

# function to print the doubly linked list 
def printList(head): 

	while (head != None) : 
		print( head.data, end = " ") 
		head = head.next
	
# function to insert a node at the 
# beginning of the doubly linked list 
def push(head_ref, new_data): 

	""" allocate node """
	new_node = Node(0) 
	
	""" put in the data """
	new_node.data = new_data 

	""" Make next of new node as head 
	and previous as None """
	new_node.next = (head_ref) 
	new_node.prev = None

	""" change prev of head node to new node """
	if ((head_ref) != None): 
		(head_ref).prev = new_node 

	""" move the head to point to the new node """
	(head_ref) = new_node 
	return head_ref 


# Driver Code 
if __name__ == "__main__": 

	""" start with the empty doubly linked list """
	head = None

	# insert the following data 
	head = push(head, 9) 
	head = push(head, 3) 
	head = push(head, 5) 
	head = push(head, 10) 
	head = push(head, 12) 
	head = push(head, 8) 

	print( "Doubly Linked List Before Sorting\n") 
	printList(head)
	print("Doubly Linked List After Sorting")
	# head = insertion_sort(head) 
	insertion_sort(head)
	printList(head) 

# This code is contributed by Arnab Kundu 
