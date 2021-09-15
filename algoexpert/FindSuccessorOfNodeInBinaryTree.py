class BinaryTree:
	def __init__(self, value):
		self.value = value
		self.right = None
		self.left = None
	

def findSuccessorOf(node, tree):
	node_list = inOrderTraversedNodes(tree)
	successor = [node_list[i+1] for i in range(len(node_list)) if node_list[i] == node and i + 1 < len(node_list)]
	return successor[0] if len(successor) > 0 else None

def inOrderTraversedNodes(tree, node_list=[]):
	if tree is not None:
		node_list = inOrderTraversedNodes(tree.left, node_list)
		node_list.append(tree.value)
		node_list = inOrderTraversedNodes(tree.right, node_list)
	
	return node_list

'''
{"id": "1", "left": "2", "parent": null, "right": "3", "value": 1},
      {"id": "2", "left": "4", "parent": "1", "right": "5", "value": 2},
      {"id": "3", "left": null, "parent": "1", "right": null, "value": 3},
      {"id": "4", "left": null, "parent": "2", "right": null, "value": 4},
      {"id": "5", "left": "6", "parent": "2", "right": "7", "value": 5},
      {"id": "6", "left": null, "parent": "5", "right": null, "value": 6},
      {"id": "7", "left": "8", "parent": "5", "right": null, "value": 7},
      {"id": "8", "left": null, "parent": "7", "right": null, "value": 8}
'''

if __name__ == '__main__':
	tree = BinaryTree(1)
	tree.left = BinaryTree(2); tree.left.left = BinaryTree(4); tree.left.left.left = BinaryTree(6)
	tree.right = BinaryTree(3); tree.left.right = BinaryTree(5)

	print(findSuccessorOf(5, tree))
