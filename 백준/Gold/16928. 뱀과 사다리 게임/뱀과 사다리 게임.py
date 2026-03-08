import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
ladder = [0] * 101
snake = [0] * 101
visited = [False] * 101
for i in range(n):
    x, y = map(int, input().split())
    ladder[x] = y
for i in range(m):
    u, v = map(int, input().split())
    snake[u] = v
q = deque()
visited[1] = True
q.append((1, 0))

while q:
    cur, cnt = q.popleft()
    if cur == 100:
        print(cnt)
        break
    for i in range(1, 7):
        nxt = cur + i
        if nxt > 100:
            continue
        # 방문 체크보다 먼저 최종 도착 칸 확정해야 함
        if ladder[nxt]:
            nxt = ladder[nxt]
        elif snake[nxt]:
            nxt = snake[nxt]
        if not visited[nxt]:
            visited[nxt] = True
            q.append((nxt, cnt + 1))
