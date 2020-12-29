def findClosestNeighbourInBst(tree, target):
	leftdiff = rightdiff = closestleft = closestright = None
	
	if target < tree.value:
		if tree.left:
			closestleft = findClosestNeighbourInBst(tree.left, target)
			leftdiff = abs(target - closestleft)
		closestroot = tree.value
		rootdiff = abs(target - closestroot)

		return closestleft if closestleft is not None and leftdiff < rootdiff else closestroot

	if target > tree.value:
		if tree.right:
			closestright = findClosestNeighbourInBst(tree.right, target)
			rightdiff = abs(target - closestright)
		closestroot = tree.value
		rootdiff = abs(target - closestroot)

		return closestright if closestright is not None and rightdiff < rootdiff else closestroot
	
	return tree.value

	
class Node:
	def __init__(self, value=None):
		self.value = value
		self.right = None
		self.left = None


	def insert(self, value):
		if self.value is not None:
			if value < self.value:
				if self.left is None:
					self.left = Node(value)
				else:
					self.left.insert(value)
			elif self.right is None:
				self.right = Node(value)
			else:
				self.right.insert(value)
		else:
			self.value = value


if __name__ == "__main__":
	BSTree = Node()
	for i in [10, 15, 22, 13, 14, 5, 5, 2, 1]:
		BSTree.insert(i)

	print(findClosestNeighbourInBst(BSTree, 12))
