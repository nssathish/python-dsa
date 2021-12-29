from DS.QueueOps import Queue


class StackWithTwoQueues:
    def __init__(self, size=0):
        self.queue1 = Queue(size)
        self.queue2 = Queue(size)
        self.size = size
    
    def push(self, item):
        try:
            self.queue2.enqueue(item)

            while not self.queue1.isEmpty():
                self.queue2.enqueue(self.queue1.dequeue())
            
            self.queue1, self.queue2 = self.queue2, self.queue1
        except OverflowError:
            print('Stack overflow')
    
    def pop(self):
        try:
            return self.queue2.dequeue()
        except ValueError:
            print('Stack is Empty')
    
    def peek(self):
        try:
            return self.queue1.peek()
        except ValueError:
            print('Stack is Empty')
    
    def isEmpty(self):
        return self.queue1.isEmpty()

    def __str__(self) -> str:
        return ','.join([ str(_) for _ in self.queue1.queue])


if __name__ == '__main__':
    S = StackWithTwoQueues(5)
    S.push(5); S.push(6); S.push(1)
    print(S.peek())
    print(S)
    S.push(4); S.push(2)
    print(S.peek())
    print(S)
