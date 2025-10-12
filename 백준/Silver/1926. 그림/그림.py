from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dx = [0, 0, -1, 1] # 상하좌우
dy = [-1, 1, 0, 0] # 상하좌우

max = 0 # 그림의 최대 넓이
cnt = 0 # 그림 수 
for i in range(n):
    for j in range(m):
        if grid[i][j] == 1 and not visited[i][j]:
            visited[i][j] = True
            q = deque([(i, j)]) # (current x, current y)
            width = 0
            cnt += 1
            while q:
                cx, cy = q.popleft()
                width += 1
                for k in range(4):
                    nx = cx + dx[k]
                    ny = cy + dy[k]
                    if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1 and not visited[nx][ny]:
                        q.append((nx, ny))
                        visited[nx][ny] = True
            if max < width:
                max = width
print(cnt)
print(max)
