n = int(input())
called = list(map(int, input().split()))

count = [0]*23

for i in called:
    count[i-1] += 1
    
for i in count:
    print(i, end=" ")