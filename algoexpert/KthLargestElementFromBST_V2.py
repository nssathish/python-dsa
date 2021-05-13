def kthLargestElementInBST(tree, k, result=None):
    result = list()
    elementsInBst(tree, k, result)
    return result[k - 1]

def elementsInBst(tree, k, result):
    if len(result) < k:
        if tree.right is not None:
            elementsInBst(tree.right, k, result)
    
        result.append(tree.value)

        if tree.left is not None:
            elementsInBst(tree.left, k, result)

    return result

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
    #print(kthLargestElementInBST(bst, 4))
