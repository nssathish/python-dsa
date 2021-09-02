class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class TreeInfo:
    def __init__(self, height, diameter):
        self.height = height
        self.diameter = diameter


def DiameterOf(tree):
    return getTreeInfo(tree).diameter


def getTreeInfo(tree):
    if tree is None:
        return TreeInfo(0, 0)

    leftTreeInfo = getTreeInfo(tree.left)
    rightTreeInfo = getTreeInfo(tree.right)

    longestPathThroughRoot = leftTreeInfo.height + rightTreeInfo.height
    maxDiameterSoFar = max(leftTreeInfo.diameter, rightTreeInfo.diameter)
    currentDiameter = max(longestPathThroughRoot, maxDiameterSoFar)
    currentHeight = max(leftTreeInfo.height, rightTreeInfo.height) + 1

    return TreeInfo(currentHeight, currentDiameter)


'''
               1
            /     \
           4       5
         /   \    / \
        4     5  6   7
             /
            8
    diameter is 5 ( 8 -> 5 -> 4 -> 1 -> 5 -> 7 or 6)
'''

if __name__ == "__main__":
    btree = BinaryTree(1)
    btree.left = BinaryTree(4); btree.left.left = BinaryTree(4); btree.left.right = BinaryTree(5); btree.left.right.left = BinaryTree(8)
    btree.right = BinaryTree(5); btree.right.left = BinaryTree(6); btree.right.right = BinaryTree(7)

    #btree = BinaryTree(1); btree.left = BinaryTree(4); btree.right = BinaryTree(5); btree.left.left = BinaryTree(3)
    print(DiameterOf(btree))
