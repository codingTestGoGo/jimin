from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

dist = [100005] * 100005
dist[n] = 0

q = deque()
q.append(n)

while q:
    x = q.popleft()
    if x == k:
        print(dist[x])
        break
    for nx, s in [(x - 1, 1), (x + 1, 1), (x * 2, 0)]:
        if 0 <= nx <= 100000:
            if dist[nx] > dist[x] + s:
                dist[nx] = dist[x] + s
                if s == 0:
                    q.appendleft(nx)
                else:
                    q.append(nx)