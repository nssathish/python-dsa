class MinStack:
	def __init__(self, size:int=0, top:int=-1):
		self.size = size
		self.top = top
		self.stack = []
		self.minStack = []
		self.minStackTop = -1
	
	def push(self, value: int) -> None:
		try:
			if self.top == self.size:
				raise ValueError("Stack Overflow")
			
			self.stack.append(value)
			self.top += 1

			if self.minStackTop == -1:
				self.minStack.append(value)
			else:
				minValue = self.minStack[self.minStackTop]
				if minValue > value:
					self.minStack.append(value)
				else:
					self.minStack.append(minValue)
			
			self.minStackTop += 1

		except ValueError as ve:
			print(ve)

	def pop(self) -> int:
		try:
			if self.isEmpty():
				raise ValueError("Stack UnderFlow")

			_ = self.minStack.pop()
			self.minStackTop -= 1
			self.top -= 1
			return self.stack.pop()
		except ValueError as ve:
			print(ve)
	
	def getMin(self) -> int:
		return None if self.isEmpty() else self.minStack[self.minStackTop]

	def isEmpty(self) -> bool:
		return self.top < 0

	def isFull(self) -> bool:
		return self.top == self.size - 1


if __name__ == '__main__':
	new_stack = MinStack(size=5)
	new_stack.push(5)
	new_stack.push(2)
	new_stack.push(10)
	new_stack.push(1)
	new_stack.push(6)
	print(new_stack.getMin())
	new_stack.pop()
	print(new_stack.getMin())
	new_stack.pop()
	print(new_stack.getMin())
	new_stack.pop()
	new_stack.pop()
	new_stack.pop()
	new_stack.pop()
	print(new_stack.getMin())