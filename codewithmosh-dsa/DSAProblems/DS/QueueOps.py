from typing import Sized


class Queue:
    def __init__(self, size=0) -> None:
        self.size = size
        self.queue = []
        self.first = 0
    
    def enqueue(self, value: int) -> None:
        try:
            if self.isFull():
                raise ValueError("Queue limit reached")
            
            self.queue.append(value)
        except ValueError as ve:
            print(ve)
    
    def dequeue(self) -> int:
        try:
            if self.isEmpty():
                raise ValueError("Queue empty")
            
            first = self.queue[self.first]
            self.queue[self.first] = 0
            self.first += 1
            return first
        except ValueError as ve:
            print(ve)
    
    def peek(self) -> int:
        try:
            if self.isEmpty():
                raise ValueError("Queue empty")

            return self.queue[0]
        except ValueError as ve:
            print(ve)
    
    def isFull(self) -> bool:
        return len(self.queue) == self.size
    
    def isEmpty(self) -> bool:
        return len(self.queue) == 0
    
    def __str__(self) -> str:
        return str(self.queue)


if __name__ == '__main__':
    new_queue = Queue(5)
    new_queue.enqueue(5); new_queue.enqueue(2); new_queue.enqueue(10); new_queue.enqueue(1); new_queue.enqueue(6)
    print(new_queue.peek())
    print(new_queue.dequeue())
    print(new_queue.peek())