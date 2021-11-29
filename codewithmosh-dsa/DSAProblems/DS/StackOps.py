class Stack:
	def __init__(self, size: int):
		self.stack = []
		self.size = size
		self.top = -1
	
	def push(self, data: str) -> None:
		try:
			if self.top < self.size - 1:
				self.stack.append(data)
				self.top += 1
			else:
				raise ValueError("Stack overflow.")
		except ValueError as ex:
			print(ex)
	
	def pop(self) -> str:
		try:
			if not self.isEmpty():
				data = self.stack.pop(self.top)
				self.top -= 1
				return data
			else:
				raise ValueError("Stack underflow.")
		except ValueError as ex:
			print(ex)
	
	def peek(self) -> str:
		try:
			if not self.isEmpty():
				return self.stack[self.top]
			else:
				raise ValueError("Stack is empty")
		except ValueError as ex:
			print(ex)
	
	def isEmpty(self) -> bool:
		return self.top < 0

	def __str__(self):
		return ",".join(self.stack)


if __name__ == '__main__':
	print('Preferred stack size:')
	size = int(input())
	new_stack = Stack(size)
	for i in range(size):
		new_stack.push(str(i))
	
	print(new_stack.top)
	new_stack.push("")
	print(new_stack.pop())
	print(new_stack)
	for i in range(size):
		new_stack.pop()
	
	print(new_stack.pop())
