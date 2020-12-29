def findClosestNeighbourInBst(tree, target, closest=None):
	if tree is None:
		return closest
	if closest is None or abs(target - tree.value) < abs(target - closest):
		closest = tree.value
	if target < tree.value:
		return findClosestNeighbourInBst(tree.left, target, closest)
	if target > tree.value:
		return findClosestNeighbourInBst(tree.right, target, closest)

	return closest
	
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

	def printTree(self):
		if self.left:
			self.left.printTree()
		print(self.value)
		if self.right:
			self.right.printTree()


if __name__ == "__main__":
	BSTree = Node()
	#for i in [100, 502, 55000, 1001, 4500, 204, 205, 207, 208, 206, 203, 5, 15, 22, 57, 60, 5, 2, 3, 1, 2, 3, 4, 5, -51, -403]:
	for i in [10, 15, 22, 13, 14, 5, 5, 2 ,1]:
		BSTree.insert(i)

	#BSTree.printTree()

	#print(findClosestNeighbourInBst(BSTree, 208))
	print(findClosestNeighbourInBst(BSTree, 12))
