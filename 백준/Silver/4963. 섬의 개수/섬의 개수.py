import sys
input = sys.stdin.readline
from collections import deque

dx = [0, 0, 1, -1, -1, -1, 1, 1] # 행방향: 동 서 남 북 북동 북서 남서 남동
dy = [1, -1, 0, 0, 1, -1, -1, 1] # 열방향: 동 서 남 북 북동 북서 남서 남동

while True:
    w, h = map(int, input().split())
    cnt = 0
    visited = [[False] * w for _ in range(h)]
    grid = [list(map(int, input().split())) for _ in range(h)]
    for i in range(h):
        for j in range(w):
            q = deque()
            if grid[i][j] and not visited[i][j]:
                q.append((i, j))
                visited[i][j] = True
                cnt += 1
                while q:
                    x, y = q.popleft()
                    for k in range(8):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] and not visited[nx][ny]:
                            visited[nx][ny] = True
                            q.append((nx, ny))
    if w == h == 0:
        break
    print(cnt)