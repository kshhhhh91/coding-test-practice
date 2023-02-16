h, w = map(int, input().split())

board = [[0]*w for i in range(h)]

n = int(input())
for i in range(n): # 막대마다
    l, d, x, y = map(int, input().split())
    for j in range(l):
        if d == 0:  # 가로방향
            board[x-1][y-1+j] = 1
        else:       # 세로방향
            board[x-1+j][y-1] = 1
            
for i in range(h):
    for j in range(w):
        print(board[i][j], end=" ")
    print()