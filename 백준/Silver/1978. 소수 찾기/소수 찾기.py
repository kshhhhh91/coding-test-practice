#1978번 소수 찾기

n = int(input())

num_list = list(map(int, input().split()))

count = n

for i in num_list:
    if i == 1:
        count -= 1
    else:
        for j in range(2, int(i**(1/2))+1):
            if i % j == 0:
                count -= 1
                break

print(count)