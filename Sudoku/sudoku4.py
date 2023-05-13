backtracks=0

def isValid(grid,i,j,e):
    rowOk= all([e != grid[i][x] for x in range(16)])
    if rowOk:
        columnOK=all(e !=grid[x][j] for x in range(16))
        if columnOK:
            secTopX, secTopY= 4*(i//4), 4*(j//4)
            for x in range(secTopX,secTopX+4):
                for y in range(secTopY,secTopY+4):
                    if grid[x][y]==e:
                        return False
            return True
    return False

def printSudoku(grid):
    numrow=0
    for row in grid:
        if numrow %4 == 0 and numrow!=0:
            print('')
        print(row[0:4],'',row[4:8],'',row[8:12],'',row[12:16])
        numrow+=1

def findNextCellToFind(grid):
    for x in range(0,16):
        for y in range(0,16):
            if grid[x][y]==-1:
                return x,y
    return -1,-1


def solveSudoku(grid, i=0, j=0):
    global backtracks
    i,j=findNextCellToFind(grid)
    if i==-1:
        return True
    for e in range(0,16):
        if isValid(grid,i,j,e):
#            impl=makeImplications(grid,i,j,e)
            grid[i][j]=e
            printSudoku(input)
            if solveSudoku(grid,i,j):
                return True
            backtracks+=1
            grid[i][j]=-1
            #undoImplications(grid,impl)

    return False

input=[[-1,-1,-1,-1,-1,6,-1,9,-1,-1,-1,1,7,-1,11,-1],
       [9,8,11,-1,-1,-1,-1,-1,3,-1,0,7,14,4,-1,-1],
       [-1,2,13,15,-1,-1,4,-1,-1,-1,-1,-1,0,1,-1,-1],
       [7,-1,-1,6,-1,-1,14,-1,10,-1,15,-1,-1,-1,-1,9],
       [14, -1, 5, 3, 9, 1, -1, -1, -1, -1, -1, 0, 11, 7, -1, -1],
       [-1, 10, -1, -1, 11, 14, -1, -1, -1, -1, -1, -1, -1, -1, -1, 5],
       [-1, -1, -1, 1, 6, 3, 5, 15, 4, 11, -1, -1, -1, -1, -1, -1],
       [-1, 12, -1, -1, -1, 10, 13, 0, -1, -1, 7, 5, 8, -1, 3, -1],
       [-1, 4, -1, 8, 12, 2, -1, -1, 7, 0, 13, -1, -1, -1, 15, -1],
       [-1, -1, -1, -1, -1, -1, 11, 3, 2, 4, 5, 8, 10, -1, -1, -1],
       [10, -1, -1, -1, -1, -1, -1, -1, -1, -1, 11, 9, -1, -1, 13, -1],
       [-1, -1, 0, 2, 8, -1, -1, -1, -1, -1, 10, 12, 3, 11, -1, 1],
       [0, -1, -1, -1, -1, 8, -1, 13, -1, 7, -1, -1, 1, -1, -1, 4],
       [-1, -1, 3, 10, -1, -1, -1, -1, -1, 12, -1, -1, 9, 8, 7, -1],
       [-1, -1, 8, 4, 5, 12, -1, 1, -1, -1, -1, -1, -1, 3, 14, 10],
       [-1, 14, -1, 13, 4, -1, -1, -1, 0, -1, 1, -1, -1, -1, -1, -1]
       ]
input2 = [[5, 1, 7, 6, 0, 0, 0, 3, 4],
 [2, 8, 9, 0, 0, 4, 0, 0, 0],
 [3, 4, 6, 2, 0, 5, 0, 9, 0],
 [6, 0, 2, 0, 0, 0, 0, 1, 0],
 [0, 3, 8, 0, 0, 6, 0, 4, 7],
 [0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 9, 0, 0, 0, 0, 0, 7, 8],
 [7, 0, 3, 4, 0, 0, 5, 6, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0]]

solveSudoku(input)
printSudoku(input)
print(backtracks)