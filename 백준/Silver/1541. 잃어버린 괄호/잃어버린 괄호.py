a = input().split('-')
answer = sum(map(int, a[0].split('+')))

for i in range(1, len(a)):
    answer -= sum(map(int, a[i].split('+')))

print(answer)