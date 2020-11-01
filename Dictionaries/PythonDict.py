#!/usr/bin/python3
"""
In a Python Dictionary
1. key is separated from it's values by colon (:)
2. the items are separated by commas
3. keys are unique within a dictionary
    values are may not be unique
4. Keys must be of immutable data type such as strings, tuples, numbers
    values can be of any type
"""

from pythonlangutil.overload import Overload,signature


class PythonDict:
    def __init__(self, pyDict):
        self.pyDict = pyDict

    def Access(self, key):
        return self.pyDict[key]

    def AddOrUpdate(self, key, value):
        self.pyDict[key] = value

    @Overload
    @signature()
    def Delete(self):
        del self.pyDict

    @Delete.overload
    @signature("str")
    def Delete(self, key: str):
        del self.pyDict[key]

    def Traverse(self):
        for key in self.pyDict.keys():
            print(f'key: {key}, value: {self.pyDict[key]}')


if __name__ == "__main__":
    testDict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
    pd = PythonDict(testDict)
    print(f'access("four"): {pd.Access("four")}')
    print('AddOrUpdate("five", 55")')
    pd.AddOrUpdate("five", 55)
    pd.Traverse()
    print('AddOrUpdate("six", 6)')
    pd.AddOrUpdate("six", 6)
    pd.Traverse()
    print('Delete("three")')
    pd.Delete("three")
    pd.Traverse()
    print('Delete()')
    pd.Delete()
