import sys
input = sys.stdin.readline
from collections import deque

s = str(input().strip())
q = deque()
need_front = 0
for bracket in s:
    if bracket == ')':
        if not q:
            need_front += 1
        else:
            q.pop()
    else:
        q.append(1)
print(len(q) + need_front)