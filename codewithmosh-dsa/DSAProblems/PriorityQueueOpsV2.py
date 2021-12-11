class PriorityQueue:
    def __init__(self, size = 0) -> None:
        if size <= 0:
            raise ValueError("Size of priority queue should be at least 1")

        self.queue = [0] * size
        self.rear = -1
    
    def enqueue(self, value: int) -> None:
        rear = self.rear
        valueNotAdded = True

        while rear >= 0 and valueNotAdded:
            if value < self.queue[rear]:
                self.queue[rear + 1] = self.queue[rear]
            else:
                self.queue[rear + 1] = value
                self.rear += 1
                valueNotAdded = False

            rear -= 1
        else:
            if valueNotAdded:
                self.queue[rear + 1] = value
                self.rear += 1


if __name__ == '__main__':
    try:
        print('PQ size: ')
        pqSize = int(input())
        new_priorityQ = PriorityQueue(pqSize)
        print(f'Enter {pqSize} element(s) to the PQ:')
        [new_priorityQ.enqueue(int(input())) for i in range(pqSize)]
        print(new_priorityQ.queue)

        '''
        new_priorityQ.enqueue(5); new_priorityQ.enqueue(2); new_priorityQ.enqueue(10); new_priorityQ.enqueue(1); new_priorityQ.enqueue(6); new_priorityQ.enqueue(0); new_priorityQ.enqueue(100); new_priorityQ.enqueue(3)
        print(new_priorityQ.queue)
        '''
    except ValueError as ve:
        print(ve)