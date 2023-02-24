n = int(input())
init_n = n

def make_newnum(n):
    sum_each = (n // 10) + (n % 10)
    newnum = ((n % 10) * 10) + (sum_each % 10)
    return newnum

n =  make_newnum(n)
cycle = 1
while n != init_n:
    n = make_newnum(n)
    cycle += 1

print(cycle)