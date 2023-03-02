M = int(input())
N = int(input())

num_list = []

for i in range(M, N+1):
    if i == 1:
        continue
    for j in range(2, int(i**(1/2))+1):
        if i % j == 0:
            break
    else:
        num_list.append(i)

if len(num_list) == 0:
    print(-1)
else:
    print(sum(num_list))
    print(min(num_list))