import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

dq = [deque([False] * 20) for _ in range(n)]

res = n
for i in range(m): # m회만큼 명령
    cmd = list(map(int, input().split()))
    if cmd[0] == 1: # 승차
        train = cmd[1] - 1
        seat = cmd[2] - 1 
        
        if dq[train][seat] == True:
            continue
        dq[train][seat] = True
        
    elif cmd[0] == 2: # 하차
        train = cmd[1] - 1
        seat = cmd[2] - 1
        
        if dq[train][seat] == False:
            continue
        dq[train][seat] = False
    elif cmd[0] == 3: # 뒤로 한 칸
        train = cmd[1] - 1
        dq[train].appendleft(False)
        dq[train].pop()
        
    elif cmd[0] == 4: # 앞으로 한 칸
        train = cmd[1] - 1
        dq[train].append(False)
        dq[train].popleft()

record = []
for i in range(n):
    duplicated = False
    for t in record:
        if t == dq[i]:
            duplicated = True
            res -= 1
            break
    if not duplicated:
        record.append(deque(dq[i]))  # 처음 보는 상태일 때만 추가

print(res)