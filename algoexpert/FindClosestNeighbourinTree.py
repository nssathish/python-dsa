'''
        10
      /    \
     5      15
   /   \   /  \
  2     5 13  22
 /          \
1            14

input dictionary from algoexpert
o
{
  "nodes": [
    {"id": "10", "left": "5", "right": "15", "value": 10},
    {"id": "15", "left": "13", "right": "22", "value": 15},
    {"id": "22", "left": null, "right": null, "value": 22},
    {"id": "13", "left": null, "right": "14", "value": 13},
    {"id": "14", "left": null, "right": null, "value": 14},
    {"id": "5", "left": "2", "right": "5-2", "value": 5},
    {"id": "5-2", "left": null, "right": null, "value": 5},
    {"id": "2", "left": "1", "right": null, "value": 2},
    {"id": "1", "left": null, "right": null, "value": 1}
  ],
  "root": "10"
}
target = 12
'''

def FineClosestNeighbourinBST(tree, target):
    closest = int(tree["root"])
    nodes = tree["nodes"]
    leftmin = None
    leftMinNode = None
    leftNode = node["left"]

    rightmin = None
    rightMinNode = None
    rightNode = node["right"]

    while leftNode:
        if leftmin is None or abs(target - int(node["left"])) < leftmin:
            leftmin = abs(target - int(node["left"])) 
            leftMinNode = node["value"]

        leftNode = node[node["left"]]

    while rightNode:
        if rightmin is None or abs(target - int(node["right"])) < rightmin)   
            rightmin = abs(target - int(node["right"]))
            rightMinNode = node["value"]

        rightNode = node[node["right"]]


    if leftmin < rightmin:
        return leftNode
    else:
        return rightNode


class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


    def insert(self, value):
        if self.data:
            if value < self.data:
                if self.left:
                    self.left.insert(value)
                else:
                    self.left = Node(value)
            elif self.right:
                self.right.insert(value)
            else:
                self.right = Node(value)
        else:
            self.data = value


    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()


if __name__ == "__main__":
    BSTree = Node()
    for i in range(10):
        BSTree.insert(i)

    BSTree.printTree()
