import MyTree.BinaryTree as bt


def branchSums(root, result=None):
	if root.left is None and root.right is None:
		return [root.data]

	if result is None:
		result = []
	if root.left is not None:
		nodeOfLeftSubTree = root.data + sum(branchSums(root.left))
		result.append(nodeOfLeftSubTree)

	if root.right is not None:
		nodeOfRightSubTree = root.data + sum(branchSums(root.right))
		result.append(nodeOfRightSubTree)

	return result


if __name__ == '__main__':
	newTree = bt.Node(1)
	newTree.left = bt.Node(2)

	newTree.left.left = bt.Node(4)
	newTree.left.left.left = bt.Node(8); newTree.left.left.right = bt.Node(9)

	newTree.left.right = bt.Node(5)
	newTree.left.right.left = bt.Node(10)

	newTree.right = bt.Node(3)
	newTree.right.left = bt.Node(6); newTree.right.right = bt.Node(7)

	#print(branchSums(newTree))
	newTree.levelOrderTraversal()
