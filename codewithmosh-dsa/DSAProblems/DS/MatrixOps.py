'''
     0   1   2   3
0    1   2   3   4
1    5   6   7   8
2    9  10  11  12
3    13 14  15  16

00 01 02 03 13 23 33 32 31 30
11 12 22 21
'''

def SpiralTraverseOf(matrix, startrow, endrow, startcolumn, endcolumn, count):

    if count > 0:
        row = startrow
        column = startcolumn
        while column < endcolumn:
            print(matrix[row][column])
            column += 1
            count -= 1
        else:
            column -= 1
        
    if count > 0:
        row += 1
        while row < endrow:
            print(matrix[row][column])
            row += 1
            count -= 1
        else:
            row -= 1
            column -= 1
    
    if count > 0:
        while column >= startcolumn:
            print(matrix[row][column])
            column -= 1
            count -= 1   
        else:
            row -= 1
            column += 1

    if count > 0:
        while row > startrow:
            print(matrix[row][column])
            row -= 1
            count -= 1

    if count > 0:
        SpiralTraverseOf(matrix, startrow + 1, endrow - 1, startcolumn + 1, endcolumn - 1, count)


if __name__ == '__main__':
    matrix = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]
    ]
    rows = len(matrix)
    columns = len(matrix[0])
    count = rows * columns
    SpiralTraverseOf(matrix, 0, rows, 0, columns, count)