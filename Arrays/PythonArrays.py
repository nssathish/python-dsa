#! /usr/bin/python3

from array import *

class PythonArray:
	"""
	Traverse - print all array elements
	Insertion - adds an element at the given index
	Deletion - Deletes an element at the given index
	Search - Searches an element using the given index or by the value
	Update - Updates an element at the given index
	"""
	def __init__(self):
		self.pyArray = array('i', [1, 3, 6, 2, 4, 7])

	def __str__(self):
		return ','.join(self.pyArray)

	def Insert(self, position, value):
		self.pyArray.insert(position, value)

	def Traverse(self):
		for x in self.pyArray:
			print(x)

	def Delete(self, index=0, value=0):
		self.pyArray.remove(value)

	def Search(self, value):
		return self.pyArray.index(value)

	def Update(self, index, value):
		self.pyArray[index] = value

if __name__ == "__main__":
	pa = PythonArray()
	print(f'{pa.pyArray}')
	pa.Insert(len(pa.pyArray) - 1, 10)
	print(f'{pa.pyArray}')
	pa.Traverse()
	pa.Delete(value=10)
	pa.Traverse()
	print(pa.Search(6))
	pa.Update(2, 90)
	pa.Traverse()
