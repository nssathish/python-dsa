class TwoStacksInOneArray:
    def __init__(self, size1: int, size2: int) -> None:
        self.stack = [""] * (size1 + size2)
        self.size1 = size1
        self.size2 = size2
        self.top1 = -1
        self.top2 = size1 - 1

    def push1(self, data: str) -> None:
        try:
            self.top1 += 1

            if self.isFull1():
                self.top1 = self.size1 - 1
                raise ValueError("Stack1 overflow.")
            
            self.stack[self.top1] = data
        except ValueError as ex:
            print(ex)
        
    def pop1(self) -> str:
        value = ""
        try:
            if self.isEmpty1():
                raise ValueError("Stack1 is empty.")
            
            value , self.stack[self.top1] = self.stack[self.top1], ""
            self.top1 -= 1

        except ValueError as ex:
            print(ex)

        return value

    def push2(self, data: str) -> None:
        try:
            self.top2 += 1

            if self.isFull2():
                self.top2 = self.size1 + self.size2 - 1
                raise ValueError("Stack2 overflow.")

            self.stack[self.top2] = data
        except ValueError as ex:
            print(ex)

    def pop2(self) -> str:
        value = ""
        try:
            if self.isEmpty2():
                raise ValueError("Stack2 is empty.")
            
            value , self.stack[self.top2] = self.stack[self.top2], ""
            self.top2 -= 1
        except ValueError as ex:
            print(ex)

        return value

    def isEmpty1(self) -> bool:
        return self.top1 < 0
    
    def isEmpty2(self) -> bool:
        return self.top2 < self.size1
    
    def isFull1(self) -> bool:
        return self.top1 == self.size1
    
    def isFull2(self) -> bool:
        return self.top2 == len(self.stack)
    
    def __str__(self) -> str:
        return ','.join(self.stack)


if __name__ == '__main__':
    new_stack = TwoStacksInOneArray(3, 4)
    new_stack.push1("1")
    new_stack.push1("2")
    print(new_stack)
    new_stack.push1("3")
    new_stack.push1("4")
    print(new_stack)
    new_stack.push2("9")
    new_stack.push2("8")
    new_stack.push2("7")
    new_stack.push2("6")
    print(new_stack)
    new_stack.push2("5")
    print(new_stack)
    new_stack.pop1()
    print(new_stack, new_stack.top1)
    new_stack.push1("1000")
    print(new_stack)