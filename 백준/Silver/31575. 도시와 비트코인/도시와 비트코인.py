import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(m)]
visited = [[False] * n for _ in range(m)]
dx = [1, 0] # 행방향 동, 남
dy = [0, 1] # 열방향 동, 남
q = deque()
q.append((0,0))
visited[0][0] = True

while (q):
    x, y = q.popleft()
    if x == m - 1 and y == n - 1:
        print('Yes')
        break
    flag = False
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] and not visited[nx][ny]:
            visited[nx][ny] = True
            q.append((nx, ny))
            flag = True
    if not flag and not q:
        print('No')           