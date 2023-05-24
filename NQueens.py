#BRANCH AND BOUND
N=8
def printSolution(board):
    print("The Board with %d Queens:" %N)
    for i in range(N):
        for j in range(N):
            print(board[i][j],end=" ")
        print()

def isSafe(row,col,slashCode,backslashCode,rowLookUp,slashCodeLookup,backslashCodeLookup):
    if(slashCodeLookup[slashCode[row][col]] or backslashCodeLookup[backslashCode[row][col]] or rowLookUp[row]):
        return False
    return True

def solveNQueensUtil(board,col,slashCode,backslashCode,rowLookUp,slashCodeLookup,backslashCodeLookup):
    #if all queens placed
    if(col>=N):
        return True
    
    for i in range(N):
        if(isSafe(i,col,slashCode,backslashCode,rowLookUp,slashCodeLookup,backslashCodeLookup)):
            # place this queen in board[i][col]
            board[i][col]=1
            rowLookUp[i]=True
            slashCodeLookup[slashCode[i][col]]=True
            backslashCodeLookup[backslashCode[i][col]]=True
            
            # recur to place rest of the queens
            if(solveNQueensUtil(board,col+1,slashCode,backslashCode,rowLookUp,slashCodeLookup,backslashCodeLookup)):
                return True
            
            #if placing the queen in board[i][col] doesn't lead to a solution, then backtrack remove queen from board[i][col]
            board[i][col]=0
            rowLookUp[i]=False
            slashCodeLookup[slashCode[i][col]]=False
            backslashCodeLookup[backslashCode[i][col]]=False
        
    #if queen can not be place in any row in this column col then return False
    return False
    

def solveNQueens():
    board=[[0 for i in range(N)] for j in range(N)]
    
    slashCode=[[0 for i in range(N)] for j in range(N)]
    
    backslashCode=[[0 for i in range(N)] for j in range(N)]
    
    rowLookUp=[False]*N #tells us which rows are occupied 
    
    # keep two arrays to tell us which diagonals are occupied
    X=2*N-1 
    slashCodeLookup=[False]*X
    backslashCodeLookup=[False]*X
    
    #initialize helper metrics
    for r in range(N):
        for c in range(N):
            slashCode[r][c]=r+c
            backslashCode[r][c]=r-c+7
            
    if(solveNQueensUtil(board,0,slashCode,backslashCode,rowLookUp,slashCodeLookup,backslashCodeLookup)==False):
        print("Solution does not exist")
        return False
    else:
        printSolution(board)
        return True
    
solveNQueens()






#BackTracking
N=8
def printSolution(board):
    print("The Board with %d Queens with BackTracking:" %N)
    for i in range(N):
        for j in range(N):
            print(board[i][j],end=" ")
        print()
        
#to check if a queen can be placed on board[row][col]
# this function is called when "col" queens are already placed in columns 
# from 0 to col -1 so we need to check only left side for attacking queens
def isSafe(board,row,col):
    # check this row on left side
    for i in range(col):
        if board[row][i]==1:
            return False
        
    # check upper diagonal on left side
    for i,j in zip(range(row,-1,-1), range(col,-1,-1)):
        if board[i][j]==1:
            return False
        
    # check lower diagonal on left side
    for i,j in zip(range(row,N,1), range(col,-1,-1)):
        if board[i][j]==1:
            return False
        
    return True

def solveNQUtil(board, col):
    # base case: if all queens are placed then return true
    if col>=N:
        return True
    
    # consider this column and try placing this queen in all rows one by one
    for i in range(N):
        
        if(isSafe(board,i,col)):
            # place this queen in board[i][col]
            board[i][col]=1
            
            # recur to place rest of the queens
            if(solveNQUtil(board,col+1)):
                return True
            
            # if placing queen in board[i][col] doesn't lead to a solution, then remove queen from board[i][col]
            board[i][col]=0
    
    #if the queen can not be placed in any row in this column col then return false
    return False
    

def solveNQ():
    board=[[0 for i in range(N)] for j in range(N)]
    
    if solveNQUtil(board,0)==False:
        print ("Solution does not exist")
        return False
    
    printSolution(board)
    return True

solveNQ()
