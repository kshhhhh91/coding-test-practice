a, d, n = map(int, input().split())

# print(a + d * (n - 1))

for i in range(n - 1):
    a = a + d
    
print(a)