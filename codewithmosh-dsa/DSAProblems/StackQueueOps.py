from DS.StackOps import Stack


class StackQueue():
    def __init__(self, size: int=0) -> None:
        self.stack1 = Stack(size)
        self.stack2 = Stack(size)

    def enqueue(self, value: int) -> None:
            self.stack1.push(str(value))
    
    def dequeue(self) -> str:
        if self.stack1.isEmpty and self.stack2.isEmpty():
            raise ValueError("Queue is empty")

        if self.stack2.isEmpty(): # **** THIS IS IMPORTANT TO MAINTAIN THE ORDER OF THE ELEMENTS IN THE QUEUE ****
            while not self.stack1.isEmpty():
                self.stack2.push(self.stack1.pop())
        
        return self.stack2.pop()
            
    def peek(self) -> str:
        return self.stack2.top()
    

if __name__ == '__main__':
    new_stack_queue = StackQueue(5)
    new_stack_queue.enqueue(5); new_stack_queue.enqueue(2); new_stack_queue.enqueue(10)
    print(new_stack_queue.dequeue())
    new_stack_queue.enqueue(1); new_stack_queue.enqueue(6)
    print(new_stack_queue.dequeue())
    print(new_stack_queue.dequeue())
    print(new_stack_queue.dequeue())
    print(new_stack_queue.dequeue())
    print(new_stack_queue.dequeue())
    print(new_stack_queue.dequeue())