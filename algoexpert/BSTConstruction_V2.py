class BST:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
	
	def insert(self, value):
				root = self
				if root is None:
					root = BST(value)
				else:
					while True:
						if value < root.value:
							if root.left is None:
								root.left = BST(value)
								break
							else:
								root = root.left
						elif value >= root.value:
							if root.right is None:
								root.right = BST(value)
								break
							else:
								root = root.right

	def remove(self, value):
		if value == self.left.value and self.left.left is None and self.left.right is None:
			self.left = None
		elif value == self.right.value and self.right.left is None and self.right.right is None:
			self.right = None
		elif self.left is not None and value < self.value:
			self.left.remove(value)
		elif self.right is not None and value > self.value:
			self.right.remove(value)
		else:
			if self.left is None and self.right is not None:
				self.value = self.right.value
				self.right = self.right.right
			elif self.right is None and self.left is not None:
				self.value = self.left.value
				self.left = self.left.left
			else:
				obj = self.right
				parent = self
				print([self.value, obj.value])
				while obj.left is not None:
					parent = obj
					obj = obj.left
				print([self.value, obj.value])
				self.value = obj.value
				if parent is self:
					parent.right = obj.right
				else:
					parent.left = obj.right

	def contains(self, value):
		root = self
		while True:
			if root is None:
				break
			if value == root.value:
				return True
			elif value < root.value:
				root = root.left
			else:
				root = root.right

		return False


	def display(self):
		root = self
                
		if self.left is not None:
			self.left.display()

		print(self.value)

		if self.right is not None:
			self.right.display()


if __name__ == "__main__":
	tree = BST(10)
	tree.insert(5); tree.insert(15); tree.insert(2); tree.insert(5); 
	tree.insert(13); tree.insert(22); tree.insert(1); tree.insert(14)
	tree.insert(12)
	tree.display()

	print(tree.contains(22))
	print(tree.contains(25))
	tree.remove(10)
	#tree.remove(13); 
	tree.display()

	newTree = BST(10)
	newTree.insert(5); newTree.insert(15); print("New Tree: "); newTree.display()
	newTree.remove(10); newTree.display()

