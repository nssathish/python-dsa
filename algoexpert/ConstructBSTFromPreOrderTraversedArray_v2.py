class TreeInfo:
	def __init__(self, rootIdx):
		self.rootIdx = rootIdx


def reconstructBst(preOrderTraversalValues):
	treeInfo = TreeInfo(0)
	
	return reconstructBSTFromRange(float("-inf"), float("inf"), preOrderTraversalValues, treeInfo)


def reconstructBSTFromRange(lowerBound, upperBound, preOrderTraversalValues, currentSubTreeInfo):
	If currentSubTreeInfo.rootIdx == len(preOrderTraversalValues):
		return None
	
	rootValue = preOrderTraversalValues[currentSubTreeInfo.rootIdx]
	if rootValue < lowerBound or rootValue >= upperBound:
		return None
	
	currentSubTreeInfo.rootIdx += 1
	leftSubTree = reconstructBSTFromRange(lowerBound, rootValue, preOrderTraversalValues, currentSubTreeInfo)
	rightSubTree = reconstructBSTFromRange(rootValue, upperBound, preOrderTraversalValues, currentSubTreeInfo)
	
	return BST(rootValue, leftSubTree, rightSubTree)