import sys
input = sys.stdin.readline

n, m = map(int, input().split())
path = []

def dfs(depth):
    if depth == m:
        print(*path)
        return
    for num in range(1, n + 1):
        path.append(num)
        dfs(depth + 1)
        path.pop()
dfs(0)