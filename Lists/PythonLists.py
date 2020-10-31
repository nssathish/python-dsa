#!/usr/local/bin/python3.8
"""
versatile data type in python
list of comma separated items in []
list need not contain values of same data type
"""
from pythonlangutil.overload import Overload, signature

class PythonLists:
	def __init__(self, pyList):
		self.pyList = pyList

	@Overload
	@signature("int")
	def access(self, index):
		return self.pyList[index]

	@access.overload
	@signature("int","int")
	def access(self, startIndex, stopIndex):
		return self.pyList[startIndex:stopIndex]

	def update(self, index, element):
		self.pyList[index] = element

	def updateList(self, startIndex, stopIndex, elements):
		self.pyList[startIndex:stopIndex] = elements

	def delete(self, index):
		del self.pyList[index]

	def deleteList(self, startIndex, stopIndex):
		del self.pyList[startIndex:stopIndex]

	def concatenateList(self, elements):
		self.pyList += elements

	def repeat(self, index, times):
		self.playList[index] *= tiems

	def exists(self, element):
		return element in self.pyList

	def traverse(self):
		for element in self.pyList: print(element)


if __name__ == "__main__":
	pl = PythonLists([1, 2, 3, 4, 5, 6, 7, 8])
	print(f'access(3): {pl.access(3)}')
	print(f'access(4, 6): {pl.access(4, 6)}')
	pl.update(4, 100)
	print(f'update(4, 100): {pl.pyList}')
	pl.updateList(1, 4, [2, 6, 8, 10])
	print(f'updateList(1, 4, [2, 6, 8, 10]): {pl.pyList}')
	pl.delete(len(pl.pyList) - 1)
	print(f'delete(len(pl.pyList) - 1): {pl.pyList}')
	pl.deleteList(3, 6)
	print(f'deleteList(3, 6): {pl.pyList}')
	pl.concatenateList([5])
	print(f'concatenateList([5]): {pl.pyList}')
	pl.concatenateList([12, 13, 14])
	print(f'concatenateList([12, 13, 14]): {pl.pyList}')
	print(f'pl.exists(13): {pl.exists(13)}')
	pl.traverse()
