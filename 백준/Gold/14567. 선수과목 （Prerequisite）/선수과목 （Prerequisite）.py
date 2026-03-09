import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
degree = [0] * (n + 1)
semester = [0] * (n + 1)
q = deque()

# 위상정렬

for i in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    degree[b] += 1 
    
for i in range(1, n + 1):
    if degree[i] == 0:
        q.append(i)
        semester[i] = 1
        
while q:
    cur = q.popleft()
    for nxt in adj[cur]:
        degree[nxt] -= 1 
        semester[nxt] = max(semester[nxt], semester[cur] + 1)
        if degree[nxt] == 0:
            q.append(nxt)
    
print(*semester[1:])