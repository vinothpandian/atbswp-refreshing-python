#! python

def printTable(tableData):

    colWidth = [0] * len(tableData)
    for i in range(len(colWidth)):
        colWidth[i] = len(max(tableData[i], key=len))

    r=0
    for col in range(len(tableData[r])):
        for row in range(len(tableData)):
            print(tableData[row][col].rjust(colWidth[row]),end=' ')
        print("")
        r+=1



tableData = [['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
