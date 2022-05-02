class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if data <= self.data:
            if self.left is None:
                self.left = BinarySearchTree(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = BinarySearchTree(data)
            else:
                self.right.insert(data)

    def delete(self, data):
        current = self
        parent = None

        while current.data != data:
            parent = current
            if data < current.data:
                current = current.left
            elif data > current.data:
                current = current.right
        else:
            if parent is None:
                if current.right is None and current.left is None:
                    self.data = None
                elif current.right is None:
                    self = self.left
                elif current.left is None:
                    self = self.right
                else:
                    self = self.right
            elif current.left is None and current.right is not None:
                if current.right.data > parent.data:
                    parent.right = current.right
                else:
                    parent.left = current.right
            elif current.left is not None and current.right is None:
                if current.left.data > parent.data:
                    parent.right = current.right
                else:
                    parent.left = current.right
            else:
                currentRight = current.right
                currentLeft = current.Left
                if currentRight.data > parent.data:
                    # Parent points to the right
                    parent.right = currentRight
                    # current node's left subtree goes to the left subtree of currentRight's left
                    while currentRight.left is not None:
                        currentRight = currentRight.left
                    else:
                        currentRight.left = currentLeft
                else:
                    # parent point to the left
                    parent.left = currentRight
                    while currentRight.left is not None:
                        currentRight = currentRight.left
                    else:
                        currentRight.left = currentLeft
                    # current node's right subtree goes to the

    def display(self):
        if self.left is not None:
            self.left.display()
        print(self.data)
        if self.right is not None:
            self.right.display()


if __name__ == '__main__':
    bst = BinarySearchTree(8)
    bst.insert(3)
    bst.insert(10)
    bst.insert(1); bst.insert(6); bst.insert(14)
    bst.insert(4); bst.insert(7); bst.insert(13)
    bst.display()
