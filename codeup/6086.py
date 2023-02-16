n = int(input())
num = 1
sum = 0

while True:
    sum += num
    num += 1
    if sum >= n:
        break

print(sum)