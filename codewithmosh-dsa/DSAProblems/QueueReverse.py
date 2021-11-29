from DS.QueueOps import Queue
from DS.StackOps import Stack

class Reverse(Queue):
    def __init__(self, size=0) -> None:
        super().__init__(size)
    
    def reverseQueue(self):
        try:
            if self.isEmpty():
                raise ValueError("Queue Empty")

            new_stack = Stack(self.size)
            while not self.isEmpty():
                new_stack.push(self.dequeue())
            
            while not new_stack.isEmpty():
                self.enqueue(new_stack.pop())

            return self.queue

        except ValueError as ve:
            return []


if __name__ == '__main__':
    new_queue = Reverse(5)
    [new_queue.enqueue(element) for element in [5, 2, 10, 1, 6]]
    print(new_queue.queue)
    print(new_queue.reverseQueue())