import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
d = deque()
for _ in range(t):
    cmd = list(input().split())
    if cmd[0] == '1':
        d.appendleft(cmd[1])
    elif cmd[0] == '2':
        d.append(cmd[1])
    elif cmd[0] == '3':
        if d:
            print(d.popleft())
        else:
            print(-1)
    elif cmd[0] == '4':
        if d:
            print(d.pop())
        else:
            print(-1)
    elif cmd[0] == '5':
        print(len(d))
    elif cmd[0] == '6':
        if d:
            print(0)
        else:
            print(1)
    elif cmd[0] == '7':
        if d:
            print(d[0])
        else:
            print(-1)
    elif cmd[0] == '8':
        if d:
            print(d[-1])
        else:
            print(-1)
        