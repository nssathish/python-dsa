class BST:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
	
	def insert(self, value):
		if value < self.value and self.left is not None:
			self.left.insert(value)
		elif value < self.value and self.left is None:
			self.left = BST(value)
		
		if value >= self.value and self.right is not None:
			self.right.insert(value)
		elif value >= self.value and self.right is None:
			self.right = BST(value)

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
		if value == self.value:
			return True
		elif value < self.value and self.left is not None:
			return self.left.contains(value)
		elif value > self.value and self.right is not None:
			return self.right.contains(value)
		else:
			return False


	def display(self):
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

