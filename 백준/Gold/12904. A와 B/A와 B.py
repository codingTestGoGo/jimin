import sys
input = sys.stdin.readline
from collections import deque

s = input().strip()
t = input().strip()

q = deque([t])
visited = {t} # set([t]) 이미 방문한 문자열 저장
flag = False
while q:
    cur = q.popleft()
    
    if cur == s:
        flag = True
        break
    
    if len(cur) < len(s):
        continue
    
    # 역연산1: 끝이 A면 A 제거
    if cur[-1] == 'A':
        nxt = cur[:-1]
        if nxt not in visited:
            visited.add(nxt)
            q.append(nxt)
    elif cur[-1] == 'B':
        nxt = cur[:-1][::-1]
        if nxt not in visited:
            visited.add(nxt)
            q.append(nxt)

print(1 if flag else 0)