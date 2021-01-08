class Node:
	def __init__(self,data=None):
		self.data = data
		self.left = None
		self.right = None

	def insert(self, data):
		if self.data:
			if data <= self.data:
				if self.left is None:
					self.left = Node(data)
				else:
					self.left.insert(data)
			else:
				if self.right is None:
					self.right = Node(data)
				else:
					self.right.insert(data)
		else:
			self.data = data
			
	def inorderTraversal(self):
		if self.left:
			self.left.inorderTraversal()
		print(self.data)
		if self.right:
			self.right.inorderTraversal()

	def levelOrderTraversal(self, nodes=None):
		nodes = [self]

		while len(nodes) != 0:
			node_in_level = nodes[0]
			del nodes[0]

			if node_in_level is not None:
				print(node_in_level.data)
				if node_in_level.left is not None:
					nodes.append(node_in_level.left)
				if self.right is not None:
					nodes.append(node_in_level.right)
