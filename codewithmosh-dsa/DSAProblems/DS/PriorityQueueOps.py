class PriorityQueue:
    def __init__(self) -> None:
        self.queue = []
        self.rear = -1

    def enqueue(self, value: int) -> None:
        if self.isEmpty():
            self.queue.append(value)
            self.rear += 1
        else:
            rear = self.rear
            while rear >= 0:
                if value < self.queue[rear]:
                    if rear + 1 == len(self.queue):
                        self.queue.append(self.queue[rear])
                        self.queue[rear] = value
                        self.rear += 1
                    else:
                        self.queue[rear + 1], self.queue[rear] = self.queue[rear], value

                    rear -= 1
                else:
                    if value >= self.queue[self.rear]:
                        self.queue.append(value)
                        self.rear += 1

                    break

    def dequeue(self) -> int:
        if self.isEmpty():
            raise ValueError("Queue Empty")

        self.rear -= 1
        return self.queue.pop(0)
    
    def isFull(self) -> bool:
        return self.rear == self.size
    
    def isEmpty(self) -> bool:
        return len(self.queue) == 0
    

if __name__ == '__main__':
    new_priorityQ = PriorityQueue()
    new_priorityQ.enqueue(5); new_priorityQ.enqueue(2); new_priorityQ.enqueue(10); new_priorityQ.enqueue(1); new_priorityQ.enqueue(6); new_priorityQ.enqueue(0); new_priorityQ.enqueue(100); new_priorityQ.enqueue(3)
    print(new_priorityQ.queue)
    new_priorityQ.dequeue()
    new_priorityQ.enqueue(1)
    print(new_priorityQ.queue)