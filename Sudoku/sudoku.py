import time
backtracks=0
sectors=[[0, 3, 0, 3], [3, 6, 0, 3], [6, 9, 0, 3],
         [0, 3, 3, 6], [3, 6, 3, 6], [6, 9, 3, 6],
        [0, 3, 6, 9], [3, 6, 6, 9], [6, 9, 6, 9]]

def undoImplications(grid,impl):
    for i in range(len(impl)):
        grid[impl[i][0]][impl[i][1]]=0

def isValid(grid,i,j,e):
    rowOk= all([e != grid[i][x] for x in range(9)])
    if rowOk:
        columnOK=all(e !=grid[x][j] for x in range(9))
        if columnOK:
            secTopX, secTopY= 3*(i//3), 3*(j//3)
            for x in range(secTopX,secTopX+3):
                for y in range(secTopY,secTopY+3):
                    if grid[x][y]==e:
                        return False
            return True
    return False

def printSudoku(grid):
    numrow=0
    for row in grid:
        if numrow %3 == 0 and numrow!=0:
            print('')
        print(row[0:3],'',row[3:6],'',row[6:9])
        numrow+=1

def makeImplications(grid,i,j,e,impl):
    global sectors
    grid[i][j]=e
    impl.append((i,j,e))
    #impl=[(i,j,e)]
    #printSudoku(grid)
    for k in range(len(sectors)):
        sectinfo=[]
        vset={1,2,3,4,5,6,7,8,9}
        for x in range(sectors[k][0],sectors[k][1]):
            for y in range(sectors[k][2],sectors[k][3]):
                if grid[x][y]!=0:
                    vset.remove(grid[x][y])
        for x in range(sectors[k][0],sectors[k][1]):
            for y in range(sectors[k][2],sectors[k][3]):
                if grid[x][y]==0:
                    sectinfo.append([x,y,vset.copy()])
        for m in range(len(sectinfo)):
            sin=sectinfo[m]
            rowv=set()
            for y in range(9):
                rowv.add(grid[sin[0]][y])
            left=sin[2].difference(rowv)
            colv=set()
            for x in range(9):
                colv.add(grid[x][sin[1]])
            left=left.difference(colv)
            if len(left)==1:
                val=left.pop()
                if isValid(grid,sin[0],sin[1],val):
                    #grid[sin[0]][sin[1]]=val
                   # impl.append((sin[0],sin[1],val))
                    impl=makeImplications(grid,sin[0],sin[1],val,impl)
    return impl

def findNextCellToFind(grid):
    for x in range(0,9):
        for y in range(0,9):
            if grid[x][y]==0:
                return x,y
    return -1,-1


def solveSudoku(grid, i=0, j=0):
    global backtracks
    i,j=findNextCellToFind(grid)
    if i==-1:
        return True
    for e in range(1,10):
        if isValid(grid,i,j,e):
            impl=[]
            impl=makeImplications(grid,i,j,e,impl)
            #time.sleep(5)
            #print(impl)
            #print("a")
            #grid[i][j]=e
            if solveSudoku(grid,i,j):
                return True
            backtracks+=1
            #grid[i][j]=0
            undoImplications(grid,impl)
            #time.sleep(20)
            #print(impl)
            #print(backtracks,"sssss")
    return False

input=[[1,0,0,0,0,0,0,8,0],
       [0,0,4,0,9,0,0,0,0],
       [0,7,0,3,0,2,0,4,0],
       [0,0,5,0,0,0,0,0,2],
       [0,8,9,0,2,3,0,5,0],
       [2,0,0,5,0,0,8,0,0],
       [0,0,7,2,0,0,0,0,0],
       [0,0,2,0,4,0,9,0,0],
       [0,5,0,7,0,0,0,2,0]]
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
