class ArrayStack:
	def __init__(self):
		self._data = []

	def __len__(self):
		return len(self._data)

	def is_empty(self):
		return len(self._data) == 0

	def push(self, e):
		self._data.append(e)

	def pop(self):
		if self.is_empty():
			raise ValueError('stack is empty')

		return self._data.pop()

	def top(self):
		if self.is_empty():
			raise ValueError('stack is empty')

		return self._data[-1]


if __name__ == "__main__":
	S = ArrayStack()
	S.push(10)
	S.push(3)
	S.push(100)

	print(S.top())
	print(S.pop())
	print(S.pop())
	print(S.pop())
	print(S.pop())	
