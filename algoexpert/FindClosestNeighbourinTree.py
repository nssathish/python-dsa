def FindClosestNeighbourinBST(tree, target):
	closest = int(tree["root"])
	treeNodes = tree["nodes"]
	nodes = {}

	for node in treeNodes:
		nodes[node["id"]] = node

	rootmin = None
	if closest:
		rootmin = target - closest

	leftmin = None
	leftMinNode = None
	leftNode = nodes[nodes[tree["root"]]["left"]]

	rightmin = None
	rightMinNode = None
	rightNode = nodes[nodes[tree["root"]]["right"]]

	while leftNode:
		if leftmin is None or abs(target - int(leftNode["value"])) < leftmin:
			leftmin = abs(target - int(leftNode["value"])) 
			leftMinNode = leftNode["value"]

		if leftNode["left"]:
			leftNode = nodes[leftNode["left"]]
		else:
			break

	while rightNode:
		if rightmin is None or abs(target - int(rightNode["value"])) < rightmin:
			rightmin = abs(target - int(rightNode["value"]))
			rightMinNode = rightNode["value"]

		if rightNode["right"]:
			rightNode = nodes[rightNode["right"]]
		else:
			break


	print([f'rootmin = {rootmin}',f'leftmin = {leftmin}', f'rightmin = {rightmin}'])
	if rootmin < leftmin and rootmin < rightmin:
		return tree["root"]
	if leftmin < rootmin and leftmin < rightmin:
		return leftNode
	if rightmin < rootmin and rightmin < leftmin:
		return rightNode


if __name__ == "__main__":
	tree = {
		"nodes": [
			{"id": "10", "left": "5", "right": "15", "value": 10},
			{"id": "15", "left": "13", "right": "22", "value": 15},
			{"id": "22", "left": None, "right": None, "value": 22},
			{"id": "13", "left": None, "right": "14", "value": 13},
			{"id": "14", "left": None, "right": None, "value": 14},
			{"id": "5", "left": "2", "right": "5-2", "value": 5},
			{"id": "5-2", "left": None, "right": None, "value": 5},
			{"id": "2", "left": "1", "right": None, "value": 2},
			{"id": "1", "left": None, "right": None, "value": 1}
		],
		"root": "10"
	}
	print(FindClosestNeighbourinBST(tree, 12))
