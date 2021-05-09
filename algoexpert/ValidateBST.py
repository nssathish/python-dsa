class BST:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
	
	def insert(self, value):
		if value < self.value:
			if self.left is not None:
				self.left.insert(value)
			else:
				self.left = BST(value)
		elif value >= self.value:
			if self.right is not None:
				self.right.insert(value)
			else:
				self.right = BST(value)
	
	def display(self):
		if self.left is not None:
			self.left.display()

		print(self.value)

		if self.right is not None:
			self.right.display()
	

def validateBst(tree):
	leftSubTreeArray = list()
	subTreeToArray(tree.left, leftSubTreeArray)
	rightSubTreeArray = list()
	subTreeToArray(tree.right, rightSubTreeArray)
	return isProperlySorted(leftSubTreeArray, tree, rightSubTreeArray)

def subTreeToArray(tree, result):
	if tree.left is not None:
		subTreeToArray(tree.left, result)

	result.append(tree.value)

	if tree.right is not None:
		subTreeToArray(tree.right, result)
	
	return result

def isProperlySorted(leftSubTreeArray, root, rightSubTreeArray):
	validLeft = validRight = True
	for i in range(1, len(leftSubTreeArray)):
		if leftSubTreeArray[i] < leftSubTreeArray[i - 1] or \
			leftSubTreeArray[i] >= root.value or \
			leftSubTreeArray[i - 1] >= root.value:
			validLeft = False
			break
	
	for i in range(1, len(rightSubTreeArray)):
		if rightSubTreeArray[i] < rightSubTreeArray[i - 1] or \
			rightSubTreeArray[i] < root.value or \
			rightSubTreeArray[i - 1] < root.value:
			validRight = False
			break
	
	return validLeft and validRight

if __name__ == "__main__":
	bst = BST(10)
	bst.left = BST(5); bst.left.left = BST(2); bst.left.right = BST(5); bst.left.right.right = BST(10)
	bst.right = BST(15); bst.right.right = BST(22); bst.right.left = BST(13)

	print(validateBst(bst))
	bst.display()
