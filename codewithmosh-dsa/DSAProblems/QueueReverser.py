from DS.QueueOps import Queue
from DS.StackOps import Stack


class QueueReverser(Queue):
    def __init__(self, queue, size=0):
        super().__init__(size)
        self.queue = queue
    
    def reverse(self, k):
        stack = Stack(k)

        i = 0
        while not stack.isFull():
            stack.push(str(self.queue[i]))
            i += 1
        print(self.queue)
        print(stack)
        
        for i in range(k):
            self.queue[i] = int(stack.pop())


if __name__ == '__main__':
    new_queue = Queue(5)
    [new_queue.enqueue(value) for value in [5, 6, 1, 4, 2]]
    queueReverser = QueueReverser(new_queue.queue, 5)
    queueReverser.reverse(3)
    print(queueReverser.queue)