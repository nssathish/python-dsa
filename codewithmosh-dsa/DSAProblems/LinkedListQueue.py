from DS.LinearLinkedListOps import LinkedList


class LinkedListQueue(LinkedList):
    _QUEUEEMPTYMESSAGE = 'Queue is empty'
    _QUEUEFULLMESSAGE = 'Queue is Full'

    def __init__(self, size=0):
        super().__init__()
        self.queueSize = size
    
    def enqueue(self, value):
        if self.isFull():
            raise OverflowError(LinkedListQueue._QUEUEFULLMESSAGE)
        
        self.addLast(value)
    
    def dequeue(self):
        if self.isEmpty():
            raise ValueError(LinkedListQueue._QUEUEEMPTYMESSAGE)
        
        self.removeFirst()
    
    def peek(self):
        if self.isEmpty():
            raise ValueError(LinkedListQueue._QUEUEEMPTYMESSAGE)
        
        return self.head.data
    
    def isFull(self):
        return self.size() == self.queueSize
    
    def isEmpty(self):
        return self.head is None


if __name__ == '__main__':
    q = LinkedListQueue(5)
    [q.enqueue(item) for item in [5, 6, 1, 4, 2]]
    q.print()
    q.dequeue(); q.dequeue()
    q.print()