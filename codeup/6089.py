a, r, n = map(int, input().split())

# print(a * r ** (n - 1))


for i in range(n - 1):
    a = a * r
    
print(a)