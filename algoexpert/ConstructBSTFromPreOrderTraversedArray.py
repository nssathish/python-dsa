def reconstructToBst(preOrderTraversedArray):
    numberOfNodes = len(preOrderTraversedArray)
    if numberOfNodes == 0:
        return None

    root = BST(preOrderTraversedArray[0])
    leftSubTreeArray = []
    rightSubTreeArray = []
    for i in range(1, numberOfNodes):
        element = preOrderTraversedArray[i]
        if element < root.value:
            leftSubTreeArray.append(element)
        else:
            rightSubTreeArray.append(element)

    root.left = reconstructToBst(leftSubTreeArray)
    root.right = reconstructToBst(rightSubTreeArray)

    return root


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def display(self):
        print(self.value)

        if self.left is not None:
            self.left.display()

        if self.right is not None:
            self.right.display()


if __name__ == "__main__":
    bst = reconstructToBst([10, 5, 2, 5, 15, 13, 14, 22])
    bst.display()
