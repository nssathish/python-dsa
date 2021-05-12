def minHeightBST(array):
    numberOfElements = len(array)

    if numberOfElements > 0 and len(array) <= 4:
        rootIdx = numberOfElements // 2
        tree = BST(array[rootIdx])
        for i in range(numberOfElements):
            if i != rootIdx:
                tree.insert(array[i])
        return tree
    else:
        rootIdx = numberOfElements // 2
        root = BST(array[rootIdx])
        leftSubTreeArray = array[0:rootIdx]
        leftSubTree = minHeightBST(leftSubTreeArray)
        rightSubTreeArray = array[rootIdx + 1:]
        rightSubTree = minHeightBST(rightSubTreeArray)
        root.left = leftSubTree
        root.right = rightSubTree
        
        return root

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)

        elif value >= self.value:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)

    def display(self):
        if self.left is not None:
            self.left.display()

        print(self.value)

        if self.right is not None:
            self.right.display()


if __name__ == "__main__":
    #minHeightTree = minHeightBST([1,2,3,4])
    minHeightTree = minHeightBST([1,2,5,7,10,13,14,15,22])
    minHeightTree.display()
