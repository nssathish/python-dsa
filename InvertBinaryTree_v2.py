class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


def LevelOrderTraverse(btree):
    queue = [btree]
    while len(queue) > 0:
        node = queue.pop(0)
        print(node.value)
        if node.left is not None: queue.append(node.left)
        if node.right is not None: queue.append(node.right)


def InvertBinaryTree(btree):
    queue = [btree]
    while len(queue) > 0:
        node = queue.pop(0)
        node.left, node.right = node.right, node.left
        if node.left is not None: queue.append(node.left)
        if node.right is not None: queue.append(node.right)

    return btree


if __name__ == "__main__":
    btree = BinaryTree(1)
    btree.left = BinaryTree(2); btree.left.left = BinaryTree(4); btree.left.right = BinaryTree(5); btree.left.right.left = BinaryTree(8)
    btree.right = BinaryTree(3); btree.right.left = BinaryTree(6); btree.right.right = BinaryTree(7)
    print("Before Inversion: "); LevelOrderTraverse(btree)
    print("After Btree Inversion: "); LevelOrderTraverse(InvertBinaryTree(btree))
    #print(InvertBinaryTree(btree))
    #print(len(InvertBinaryTree(btree)))
