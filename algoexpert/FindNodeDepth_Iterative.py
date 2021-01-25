def nodeDepth(root):
    queue = [[root, 0]]
    depth = 0

    while len(queue) > 0:
        item = queue.pop()
        node = item[0]
        nodeDepth = item[1]

        depth += nodeDepth

        if node.left:
            queue.append([node.left, nodeDepth + 1])

        if node.right:
            queue.append([node.right, nodeDepth + 1])

    return depth
