board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]

mLen = len(board)
nLen = len(board[0])
result = []
for m, item in enumerate(board):
    temp = []
    for n in range(nLen):
        neigbor = 0
        neigbor += board[m-1][n-1] if(m != 0 and n != 0 and m-1 < mLen and n-1 < nLen) else 0
        neigbor += board[m-1][n] if(m != 0 and m-1 < mLen and n < nLen) else 0
        neigbor += board[m-1][n+1] if(m != 0 and m-1 < mLen and n+1 < nLen) else 0
        neigbor += board[m][n-1] if(n != 0 and m < mLen and n-1 < nLen) else 0
        neigbor += board[m][n+1] if(m < mLen and n+1 < nLen) else 0
        neigbor += board[m+1][n-1] if(n != 0 and m+1 < mLen and n-1 < nLen) else 0
        neigbor += board[m+1][n] if( m+1 < mLen and n < nLen) else 0
        neigbor += board[m+1][n+1] if(m+1 < mLen and n+1 < nLen) else 0
        if(board[m][n] == 0):
            if(neigbor == 3):
                temp.append(1)
            else:
                temp.append(0)
        else:
            if(neigbor<2):
                temp.append(0)
            elif(neigbor ==2 or neigbor == 3):
                temp.append(1)
            else:
                temp.append(0)
    result.append(temp)

for m, item in enumerate(board):
    for n in range(nLen):
        board[m][n] = result[m][n]