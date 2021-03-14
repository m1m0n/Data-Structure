from queue import Queue

if __name__ == '__main__':
	queue = []
	print(queue)
	queue.append(28)
	queue.append(25)
	queue.append(29)
	print(queue)

	print(queue.pop(0))
	print(queue)
	print("-"*15)

	q = Queue(maxsize=5)
	print(q.qsize())
	q.put(1)
	q.put(2)
	q.put(3)
	q.put(4)
	q.put(5)
	print(q.qsize())
	print(q.full())
	print(q.get())
	print(q.get())
	print(q.get())

	print(q.empty())