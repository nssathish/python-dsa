from Node import Node

class LinkedList:
	def __init__(self, data):
		self.head = Node(data)
		self.tail = self.head
	
	def addLast(self, data):
		self.tail.next = Node(data)
		self.tail = self.tail.next
	
	def addFirst(self, data):
		oldHead = self.head
		self.head = Node(data)
		self.head.next = oldHead
	
	def indexOf(self, data):
		idx = None
		if self.head.data == data:
			idx = 0
		else:
			head = self.head
			while head is not None and head.data != data:
				if idx is None: idx = 0
				head = head.next
				idx += 1

		return idx
	
	def contains(self, data):
		return False if self.indexOf(data) is None else True
	
	def removeFirst(self):
		self.head = self.head.next
	
	def removeLast(self):
		head = self.head
		while head.next is not self.tail:
			head = head.next

		head.next = None
		self.tail = head

	def size(self):
		count = 0
		head = self.head
		while head is not None:
			count += 1
			head = head.next

		return count

	def print(self):
		head = self.head
		items = []
		while head is not None:
			items.append(str(head.data))
			head = head.next

		print(' -> '.join(items))


if __name__ == '__main__':
	newList = LinkedList(1)
	newList.addLast(2); newList.addLast(3); newList.addLast(4)
	newList.print()
	newList.addFirst(0)
	print(newList.head.data)
	print(f'size: {newList.size()}')
	newList.print()

	print(f' index of 3: {newList.indexOf(3)}')
	print(f' list contains 4?: {newList.contains(4)}')
	newList.removeFirst(); print('removed first element')
	newList.print()
	newList.removeLast(); print('removed last element')
	print(f'size: {newList.size()}')
	newList.print()
	print(f'size: {newList.size()}')



