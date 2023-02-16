n = int(input())
called = list(map(int, input().split()))

for i in range(n-1, -1, -1):
    print(called[i], end=" ")