#!/usr/bin/python3
"""
Matrix is a special case of 2D array
1. elements are of strictly same size.
2. every matrix is a 2D array BUT ever 2D array may not be a matrix
"""

from multipledispatch import dispatch
from numpy import *
from abc import ABC,abstractmethod


class PythonMatrices(IPythonMatrices):
    def __init__(self, rows, columns, pyMatrix):
        self.pyMatrix = pyMatrix
        self.rows = rows
        self.columns = columns


    @dispatch(ndarray)
    def Add(self, rows):
        pass

    @dispatch(array)
    def Add(self, columns):
        pass

    @dispatch(array)
    def Update(self, row):
        pass

    @dispatch(array)
    def Update(self, column):
        pass

    @dispatch(array)
    def Delete(self, row):
        pass


if __name__ == "__main__":
    pm = PythonMatrices(5, 5, array([['Mon', 10, 11, 12], ['Tue', 13, 14, 15]]))
