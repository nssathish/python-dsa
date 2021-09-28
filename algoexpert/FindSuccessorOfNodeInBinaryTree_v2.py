class BinaryTree:
	def __init__(self, value, parent=None):
		self.value = value
		self.parent = parent
		self.right = None
		self.left = None


def findSuccessor(node, tree):
	if node.right is not None:
		return leftMostNodeIn(node.right)

	return oldestAncestorOf(node)


def leftMostNodeIn(tree):
	currentNode = tree
	while currentNode.left is not None:
		currentNode = currentNode.left

	return currentNode


def oldestAncestorOf(tree):
	currentNode = tree
	while currentNode.parent is not None and currentNode.parent.right == currentNode:
		currentNode = currentNode.parent

	return currentNode.parent

	
if __name__ == "__main__":
	btree = BinaryTree(1)
	btree.left = BinaryTree(2, btree) 
	btree.right = BinaryTree(3, btree)
	btree.right.left = BinaryTree(4, btree.right); btree.right.left.left = BinaryTree(5, btree.right.left.left)
	btree.right.left.left.left = BinaryTree(6, btree.right.left.left)
	btree.right.left.left.left.left = BinaryTree(7, btree.right.left.left.left)

	print(findSuccessor(BinaryTree(2, btree), btree).value)
