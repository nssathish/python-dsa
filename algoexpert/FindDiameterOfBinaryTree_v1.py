class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


def Diameter(tree):
    queue = [tree]
    diameter = 0

    while len(queue) > 0:
        node = queue.pop(0)
        currentDiameter = heightOf(node.left) + heightOf(node.right)
        if diameter < currentDiameter:
            diameter = currentDiameter

        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

    return diameter


def heightOf(node):
    if node is None:
        return 0

    lh = heightOf(node.left)
    rh = heightOf(node.right)

    return max(lh, rh) + 1 


'''
              1
            /   \
           4     5
         /   \
        3     5
       /       \
      2         6
     /           \
    0             7
    diameter is 6 ( 0 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 )
'''

if __name__ == "__main__":
    btree = BinaryTree(1)
    btree.left = BinaryTree(4); 
    btree.left.left = BinaryTree(3); btree.left.left.left = BinaryTree(2);
    btree.left.right = BinaryTree(5); btree.left.right.right = BinaryTree(6); btree.left.right.right.right = BinaryTree(7)
    btree.right = BinaryTree(5)

    #btree = BinaryTree(1); btree.left = BinaryTree(4); btree.right = BinaryTree(5); btree.left.left = BinaryTree(3)
    print(Diameter(btree))
