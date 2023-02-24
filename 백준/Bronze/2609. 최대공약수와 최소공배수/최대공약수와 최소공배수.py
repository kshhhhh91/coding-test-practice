def gcd(a, b):
    while a:
        if a < b:
            a, b = b, a
        a = a % b
    return b

a, b = map(int, input().split())

G = gcd(a, b)
L = int((a * b) / G)

print(G, L, sep="\n")