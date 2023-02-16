# 16진수 구구단

n = int(input(), 16)

for i in range(1, 16):
    print("%X*%X=%X"%(n, i, n * i))