import sys

n = int(input())
arr = sorted(list(input().split() for _ in range(n)), key = lambda x : (int(x[1]), int(x[0])))
for i in arr:
    print(i[0], i[1])
