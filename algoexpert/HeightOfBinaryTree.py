class BinaryTree:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None


def heightOf(btree):
	if btree is None:
		return 0
	
	leftHeight = heightOf(btree.left)
	rightHeight = heightOf(btree.right)

	return max(leftHeight, rightHeight) + 1


if __name__ == "__main__":
	btree = BinaryTree(1)
	btree.left = BinaryTree(2); btree.left.left = BinaryTree(4); btree.left.right = BinaryTree(5)
	btree.right = BinaryTree(3); btree.right.left = BinaryTree(6); btree.right.right = BinaryTree(7)

	print(heightOf(btree))
