w, h, b = map(int, input().split())

print(format(w*h*b/8/1024/1024, ".2f"), "MB")

# print(round(w*h*b/8/1024/1024, 2), "MB") -> 0.00 MB 에서 테스트케이스 탈락