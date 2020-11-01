"""
Two Dimensional Array
1. array of arrays
2. position is referred by 2 indices
3. represents tables with rows and columns
"""

from pythonlangutil.overload import Overload,signature
from array import *


class Python2DArray:
    def __init__(self, pyArray):
        self.pyArray = pyArray

    @Overload
    @signature("int","int")
    def Access(self, rowIndex, columnIndex):
        return self.pyArray[rowIndex][columnIndex]

    @Access.overload
    @signature("int")
    def Access(self, rowIndex):
        return self.pyArray[rowIndex]

    @Overload
    @signature("int","int","int")
    def Update(self, rowIndex, columnIndex, element):
        try:
            self.pyArray[rowIndex][columnIndex] = element
        except KeyError as ke:
            print(f'Message: {ke.message}')

    @Update.overload
    @signature("int","array")
    def Update(self, rowIndex, elements: array):
        try:
            self.pyArray[rowIndex] = elements
        except KeyError as ke:
            print(f'Message: {ke.message}')

    def Delete(self, rowIndex, columnIndex):
        try:
            del self.pyArray[rowIndex][columnIndex]
        except KeyError as ke:
            print(f'Message: {ke.message}')

    def DeleteArray(self, rowIndex):
        try:
            del self.pyArray[rowIndex]
        except KeyError as ke:
            print(f'Message: {ke.message}')

    def Traverse(self):
        for row in self.pyArray:
            for column in row:
                print(column, end=" ")
            print()


if __name__ == "__main__":
    p2d = Python2DArray([[11,12, 5, 2], [15, 6, 10], [10, 8, 12, 5], [12, 15, 8, 6]])
    print(f'access(2,2): {p2d.Access(2,2)}')
    print(f'access(3): {p2d.Access(3)}')
    print('Update(1,1,100');p2d.Update(1,1,100);p2d.Traverse()
    print('Update(2, [99,99,99]');p2d.Update(2, array('i',[99,99,99]));p2d.Traverse()
    print('Delete(3,2)');p2d.Delete(3, 2);p2d.Traverse()
    print('DeleteArray(0)');p2d.DeleteArray(0);p2d.Traverse()

