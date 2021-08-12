class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def levelOrderTraverse(btree):
    queue = [btree]

    while len(queue) > 0:
        node = queue.pop(0)
        print(node.value)
        if node.left is not None: queue.append(node.left)
        if node.right is not None: queue.append(node.right)


if __name__ == '__main__':
    btree = BinaryTree(1)
    btree.left = BinaryTree(2); btree.right = BinaryTree(3)
    btree.left.left = BinaryTree(4); btree.left.right = BinaryTree(5)
    btree.right.left = BinaryTree(6); btree.right.right = BinaryTree(7)

    levelOrderTraverse(btree)
