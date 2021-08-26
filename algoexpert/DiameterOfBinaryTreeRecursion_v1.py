class BinaryTree:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None


def diameterOf(btree):
	queue = [btree]
	diameter = 0

	while len(queue) > 0:
		node = queue.pop(0)
		diameterForNode = heightOf(node.left) + heightOf(node.right)
		if diameter < diameterForNode:
			diameter = diameterForNode

		if node.left is not None:
			queue.append(node.left)
		if node.right is not None:
			queue.append(node.right)
	
	return diameter

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

	print(diameterOf(btree))
