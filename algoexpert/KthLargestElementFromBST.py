def kthLargestElementInBST(tree, k):
    result = list()
    ElementsInBst(tree, result)
    print(result)
    return result[k - 1]

def ElementsInBst(tree, result):
    if tree.right is not None:
        ElementsInBst(tree.right, result)
    
    result.append(tree.value)

    if tree.left is not None:
        ElementsInBst(tree.left, result)

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
        else:
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
    bst = BST(10);
    bst.insert(5); bst.insert(15); bst.insert(5); bst.insert(2); bst.insert(5)
    bst.insert(14); bst.insert(13); bst.insert(22)

    print(kthLargestElementInBST(bst, 3))
