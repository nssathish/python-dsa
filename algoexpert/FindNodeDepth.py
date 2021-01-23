import MyTree.BinaryTree as bt
'''
                1
        2               3
    4       5      6         7
 8     9

5 steps to solve recursive problem
----------------------------------
1. what is the simplest possible input? - the base case
2. play around with examples and visualize
3. Relate hard cases to simpler cases
4. Generalize the pattern
5. Write code by combining recursive pattern with the base case

'''
def nodeDepths(root, depth=0):
    if root:
        return depth + nodeDepths(root.left, depth + 1) + nodeDepths(root.right, depth + 1)

    return 0


if __name__ == '__main__':
	newTree = bt.Node(1)
	newTree.left = bt.Node(2)

	newTree.left.left = bt.Node(4)
	newTree.left.left.left = bt.Node(8); newTree.left.left.right = bt.Node(9)

	newTree.left.right = bt.Node(5)
	#newTree.left.right.left = bt.Node(10)

	newTree.right = bt.Node(3)
	newTree.right.left = bt.Node(6); newTree.right.right = bt.Node(7)

	# expected output 16
	print(nodeDepths(newTree))
	newTree.levelOrderTraversal()
