board = []

for i in range(19):
    board.append(list(map(int, input().split())))  # 입력을 리스트 형태로 만들기

n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    for j in range(19):    # 뒤집기
        if board[j][y-1] == 0:
            board[j][y-1] = 1
        else:
            board[j][y-1] = 0
        if board[x-1][j] == 0:
            board[x-1][j] = 1
        else:
            board[x-1][j] = 0

for i in range(19):
    for j in range(19):
        print(board[i][j], end=" ")
    print()