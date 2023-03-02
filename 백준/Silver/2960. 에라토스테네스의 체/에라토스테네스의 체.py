# 2960번 에라토스테네스의 체

N, K = map(int, input().split())

num_list = [i for i in range(2, N+1)]


while K != 0:
    P = min(num_list)
    i = P
    num_list.remove(P)
    K -= 1
    if K == 0:
        break
    for i in num_list:
        if i % P == 0:
            num_list.remove(i)
            K -= 1
        if K == 0:
            break

print(i)