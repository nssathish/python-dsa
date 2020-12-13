class Node:
    def __init__(self, data:int = None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.current = None

    def addNode(self, value):
        if self.head is None:
            self.head = Node(value)
            self.current = self.head
        else:
            self.current.next = Node(value)
            self.current = self.current.next

    def updateNode(self, fromValue, toValue) -> bool:
        self.current = self.head
        isFoundedAndUpdated = False

        while self.current is not None:
            if self.current.data == fromValue:
                self.current.data = toValue
                isFoundedAndUpdated = True
            else:
                self.current = self.current.next

        return isFoundedAndUpdated

    def deleteNode(self, value):
        self.current = self.head
        previousNode = Node()
        while self.current is not None and self.current.data != value:
            previousNode = self.current
            self.current = self.current.next
        
        if self.current is not None:
            previousNode.next = self.current.next
            self.current.data = previousNode.data
            self.current.next = previousNode.next

            return True
        else:
            return False


    def display(self):
        parseNode = self.head
        while (parseNode):
            print(parseNode.data)
            parseNode = parseNode.next


if __name__ == "__main__":
    linkedList = SinglyLinkedList()
    for i in range(10):
        linkedList.addNode(i)

    linkedList.display()
    if linkedList.updateNode(0, 1):
        print('Updated Linked link list for 0 -> 1 and the new list is: ')
        linkedList.display()
    else:
        print(f'Element "{0}" does not exist in the list')

    if linkedList.deleteNode(1):
        print('Delete Linked link list of the Node with data: 1 and the new list is: ')
        linkedList.display()
    else:
        print(f'Element "{0}" does not exist in the list')
