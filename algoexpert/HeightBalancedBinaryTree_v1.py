class BinaryTree:
	def __init__(self, value, left = None, right = None):
		self.value = value
		self.right = right
		self.left = left

def heightBalancedBinaryTree(tree):
	queue = [tree]
	while len(queue) > 0:
		node = queue.pop(0)
		heightOfLeftSubTree = HeightOf(node.left)
		heightOfRightSubTree = HeightOf(node.right)
		print(f'(heightofleftsubtree: {heightOfLeftSubTree}, heightofrightsubtree: {heightOfRightSubTree})')

		if abs(heightOfLeftSubTree - heightOfRightSubTree) > 1:
			return False
		
		if node.left is not None:
			queue.append(node.left)
		if node.right is not None:
			queue.append(node.right)

	return True

def HeightOf(tree):
	if tree is None:
		return 0
	
	return max(HeightOf(tree.left), HeightOf(tree.right)) + 1


if __name__ == '__main__':
	btree = BinaryTree(1)
	btree.left = BinaryTree(2)
	btree.right = BinaryTree(3)
	btree.right.left = BinaryTree(4); btree.right.left.left = BinaryTree(5); btree.right.left.left.left = BinaryTree(6)

	print(heightBalancedBinaryTree(btree))
