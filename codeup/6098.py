cave = []

for i in range(10):
    cave.append(list(map(int, input().split())))  # 입력을 리스트 형태로 만들기
    
x, y = 1, 1

while cave[x][y] != 2:   # 좌표의 값이 2가 나올 때까지 반복
    cave[x][y] = 9
    if cave[x][y+1] == 0 or cave[x][y+1] == 2:  # 오른쪽으로 갔을 때 0 or 2라면 오른쪽으로 가기
        y += 1
    elif cave[x+1][y] == 0 or cave[x+1][y] == 2: # 아래로 갔을 때 0 or 2라면 아래로 가기
        x += 1
    else:  # 오른쪽, 아래 둘 다 1로 막혀있으면 멈추기
        break
    
cave[x][y] = 9

for i in range(10):
    for j in range(10):
        print(cave[i][j], end=" ")
    print()