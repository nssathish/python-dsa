#!/usr/local/bin/python3.8

"""
Tuples are:
sequence of immutable objects
so tuples cannot be cahnged (unlike lists)
tuples uses parenthesis (unlike square braces in lists)
tuple can have items of different data type
single element in a tuple shoule have (,) comma after the first element
	like newTuple = (50,)
"""

from pythonlangutil.overload import Overload,signature


class PythonTuples:
	def __init__(self, newTuple):
		self.newTuple = newTuple

	def Traverse(self):
		for item in self.newTuple: print(item)

	def Update(self, elements):
		return self.newTuple + elements

	@Overload
	@signature()
	def Delete(self):
		del self.newTuple

	#This operation is not possible with tuples
	#since tuples are immutable
	#def Update(self, index,element):
	#	self.newTuple[index] = element

	#@Delete.overload
	#@signature("int")
	#def Delete(self, index):
	#	del self.newTuple[index]

	#This operation is not possible with tuples
	#since tuples are immutable
	#def Update(self, index,element):
	#	self.newTuple[index] = element

	def exists(self, element):
		return element in self.newTuple


if __name__ == "__main__":
	pt = PythonTuples((1,2,3,4,5,6))
	print('newTuple Traverse:')
	pt.Traverse()
	print('newTuple update(tuple([99,98,97]))')
	print(pt.Update((99,98,97)))
	print(f'newTuple exists(99)? : {pt.exists(99)}')
	print(f'newTuple exists(5)? : {pt.exists(5)}')
	print('newTuple delete(5)')
	pt.Delete(); print(pt.newTuple)
