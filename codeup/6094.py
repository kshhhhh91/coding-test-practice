n = int(input())
called = list(map(int, input().split()))
min = called[0]

for i in called:
    if i < min:
        min = i

print(min)