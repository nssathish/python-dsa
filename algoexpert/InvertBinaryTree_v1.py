class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


def InvertBinaryTree(btree):
    if btree is None:
        return None
    else:
        btree.left, btree.right = btree.right, btree.left

    InvertBinaryTree(btree.left)
    InvertBinaryTree(btree.right)
    return btree


def LevelOrderTraverse(btree):
    queue = [btree]
    while len(queue) > 0:
        node = queue.pop(0)
        print(node.value)
        if node.left is not None: queue.append(node.left)
        if node.right is not None: queue.append(node.right)


if __name__ == "__main__":
    btree = BinaryTree(1)
    btree.left = BinaryTree(2); btree.left.left = BinaryTree(4); btree.left.right = BinaryTree(5); btree.left.right.left = BinaryTree(8)
    btree.right = BinaryTree(3); btree.right.left = BinaryTree(6); btree.right.right = BinaryTree(7)
    LevelOrderTraverse(InvertBinaryTree(btree))

