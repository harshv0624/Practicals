N=int(input("Enter number of queens: "))
board=[[0] * N for i in range(N)]

def isSafe(board,row,col,n):
    for i in range(row):
        if board[i][col]==1:
            return False
        
    i,j=row,col
    while i>=0 and j>=0:
        if board[i][j]==1:
            return False
        i-=1
        j-=1
    i,j=row,col
    while i>=0 and j<n:
        if board[i][j]==1:
            return False
        i-=1
        j+=1
    
    return True

def Nqueens(board,row,n):
    if row>=n:
        return True
    for col in range(n):
        if isSafe(board,row,col,n):
            board[row][col]=1
            if Nqueens(board,row+1,n):
                return True
        board[row][col]=0
    return False

if Nqueens(board,0,N):
    print("Solution Found")
    for row in board:
        print(row)
else:
    print("no")
