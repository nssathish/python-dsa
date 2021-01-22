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
    if root.left and root.right:
        depth = depth + nodeDepths(root.left, depth + 1) + nodeDepths(root.right, depth + 1)
    elif root.left:
        depth += nodeDepths(root.left, depth + 1)
    elif root.right:
        depth += nodeDepths(root.right, depth + 1)

    return depth
