'''
			10
		      
         5      15
               
      2    5  13   22
               
			 12  14
'''
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
		root = self

		if value == root.value:
			if root.left is None and root.right is not None:
				root.value = root.right.value
				root.right = root.right.right
			elif root.right is None and root.left is not None:
				root.value = root.left.value
				root.left = root.left.left
			elif root.right is not None and root.left is not None:
				(successor, parent) = root.find_successor(root.right)
				root.value = successor.value
				if parent is root:
					parent.right = successor.right
				else:
					parent.left = successor.right
		else:
			while True:
				if root is None:
					break

				if value < root.value:
					parent = root
					root = root.left
				elif value > root.value:
					parent = root
					root = root.right
				else:
					(successor, parent) = root.find_successor(root.right)
					root.value = successor.value
					parent.left = successor.right
					break

	def find_successor(self, node):
		parent = self
		while node.left is not None:
			parent = node
			node = node.left

		return (node, parent)

	def contains(self, value):
		root = self
		while True:
			if root is None:
				return False
			if value == root.value:
				return True
			elif value < root.value:
				root = root.left
			else:
				root = root.right

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

