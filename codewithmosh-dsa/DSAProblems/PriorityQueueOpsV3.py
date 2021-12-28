class PriorityQueueOpsV3:
    def __init__(self, size=0) -> None:
        self.queue = [0] * size
        self.size = size
        self.count = 0
    
    def enqueue(self, item):

        if self.isFull():
            raise OverflowError('Queue is full')

        i = self.shiftItemsToInsert(item)
        self.queue[i] = item
        self.count += 1
    
    def remove(self):

        if self.isEmpty():
            raise ValueError('Queue is Empty')
        
        self.queue[self.count - 1] = 0
        self.count -= 1

    def shiftItemsToInsert(self, item):
        i = self.count - 1
        while i >= 0:
            if self.queue[i] > item:
                self.queue[i + 1] = self.queue[i]
            else:
                break

            i -= 1
        
        return i + 1

    def isEmpty(self):
        return self.count == 0
    
    def isFull(self):
        return self.count == self.size


if __name__ == '__main__':
    print('PQ size: ')
    pqSize = int(input())
    new_priorityQ = PriorityQueueOpsV3(pqSize)
    print(f'Enter {pqSize} element(s) to the PQ:')
    [new_priorityQ.enqueue(int(input())) for i in range(pqSize)]
    print(new_priorityQ.queue)
    [new_priorityQ.remove() for i in range(new_priorityQ.count)]
    print(new_priorityQ.queue)
    new_priorityQ.remove()
