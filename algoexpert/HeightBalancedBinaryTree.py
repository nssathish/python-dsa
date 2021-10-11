class BinaryTree:
      def __init__(self, value):
            self.left = None
            self.right = None
            self.value = value


class TreeInfo:
      def __init__(self, isBalanced, height):
            self.isBalanced = isBalanced
            self.height = height


def isHeightBalancedTree(btree):
      return getTreeInfo(btree).isBalanced

def getTreeInfo(btree):
      if btree is not None:
            leftSubTreeInfo = getTreeInfo(btree.left)
            rightSubTreeInfo = getTreeInfo(btree.right)

            isTreeBalanced = leftSubTreeInfo.isBalanced and rightSubTreeInfo.isBalanced and abs(leftSubTreeInfo.height - rightSubTreeInfo.height) <= 1
            heightOfTree = max(leftSubTreeInfo.height, rightSubTreeInfo.height) + 1

            return TreeInfo(isTreeBalanced, heightOfTree)
      
      return TreeInfo(True, 0)


'''
                  1
              /       \
             2         3
           /         /   \
          4         6     7
         /
        5
'''

if __name__ == '__main__':
      tree = BinaryTree(1)
      tree.left = BinaryTree(2); tree.left.left = BinaryTree(4); tree.left.left.left = BinaryTree(5)
      tree.right = BinaryTree(3); tree.right.left = BinaryTree(6); tree.right.right = BinaryTree(7)

      print(isHeightBalancedTree(tree))