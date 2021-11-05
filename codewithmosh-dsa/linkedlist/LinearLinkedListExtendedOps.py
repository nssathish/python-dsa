from LinearLinkedListOps import LinkedList

class LinkedListExtension(LinkedList):
	def __init__(self, data):
		super().__init__(data)

	def reverse(self):
		linked_list = self.head
		_ = []
		while linked_list is not None:
			_.append(linked_list.data)
			linked_list = linked_list.next

		linked_list = self.head
		for item in reversed(_):
			linked_list.data = item
			linked_list = linked_list.next

	def reverse_v2(self):
		previousNode = self.head
		currentNode = previousNode.next
		previousNode.next = None
		while currentNode is not None:
			nextNode = currentNode.next
			currentNode.next = previousNode
			previousNode = currentNode
			currentNode = nextNode

		self.head = previousNode

	def KthNodeFromEnd(self, k):
		if k < 0: return None

		currentNode = self.head
		nextNode = self.head
		
		i = 0
		while i < k and nextNode is not None:
			nextNode = nextNode.next
			i += 1

		while nextNode is not None:
			currentNode = currentNode.next
			nextNode = nextNode.next

		return currentNode.data
	
	def printMiddle(self):
		currentNode = self.head
		nextNode = currentNode.next

		if nextNode.next is None: return []

		while nextNode.next is not None:
			currentNode = currentNode.next
			nextNode = nextNode.next.next
			if nextNode is None: return []

		return [currentNode.data, currentNode.next.data]

	def createLoop(self):
		self.tail.next = self.head

	def hasLoop(self):
		currentNode = self.head
		nextNode = currentNode.next.next
		while nextNode is not None and currentNode != nextNode:
			currentNode = currentNode.next
			nextNode = nextNode.next.next
		
		return True if currentNode == nextNode else False


if __name__ == '__main__':
	newList = LinkedListExtension(0)
	newList.addLast(1); newList.addLast(2); newList.addLast(3); newList.addLast(4)
	newList.print()
	#newList.reverse() # O(n) space complexity
	newList.reverse_v2() # O(1) space complexity
	newList.print()
	print(newList.KthNodeFromEnd(2))
	print(newList.printMiddle())
	newList.addLast(5)
	print(newList.printMiddle())
	newList.createLoop()
	print(newList.hasLoop())
