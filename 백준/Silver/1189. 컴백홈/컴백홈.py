import sys
input = sys.stdin.readline

r, c, k = map(int, input().split())
grid = [[] * c  for _ in range(r)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(r):
    grid[i] = list(input().strip())

visited = [[False] * c for _ in range(r)]
res = 0; # k인 가짓수

def dfs(cx, cy, cdist):
    global res
    if cx == 0 and cy == c - 1 and cdist == k:
        res += 1
        return
        
    for i in range(4):
        nx, ny = cx + dx[i], cy + dy[i]
        if 0 <= nx < r and 0 <= ny < c and grid[nx][ny] != 'T' and not visited[nx][ny]:
            visited[cx][cy] = True
            dfs(nx, ny, cdist + 1)
            visited[cx][cy] = False

dfs(r - 1, 0, 1) # start
print(res)