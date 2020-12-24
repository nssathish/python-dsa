class Node:
	def __init__(self,data=None):
		self.data = data
		self.left = None
		self.right = None

	def insert(self, data):
		if self.data:
			if data <= self.data:
				if self.left is None:
					self.left = Node(data)
				else:
					self.left.insert(data)
			else:
				if self.right is None:
					self.right = Node(data)
				else:
					self.right.insert(data)
		else:
			self.data = data
			
					
	def inorderTraversal(self):
		if self.left:
			self.left.inorderTraversal()
		print(self.data)
		if self.right:
			self.right.inorderTraversal()


if __name__ == "__main__":
	newTree = Node()
	items = list(map(int, "8 5 2 6 9 3 5 4 8 7".split(' ')))
	for i in range(len(items)):
		newTree.insert(items[i])
	newTree.inorderTraversal()
