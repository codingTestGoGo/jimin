import sys
input = sys.stdin.readline

r, c, k = map(int, input().split())
grid = [list(input().strip()) for _ in range(r)]
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

visited = [[False] * c for _ in range(r)]
res = 0 # k인 가짓수

def dfs(cx, cy, cdist):
    global res
    
    if cdist == k: 
        if cx == 0 and cy == c - 1:
            res += 1
        return
        
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = cx + dx, cy + dy
        if 0 <= nx < r and 0 <= ny < c and grid[nx][ny] != 'T' and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, cdist + 1)
            visited[nx][ny] = False

visited[r - 1][0] = True
dfs(r - 1, 0, 1) # start
print(res)