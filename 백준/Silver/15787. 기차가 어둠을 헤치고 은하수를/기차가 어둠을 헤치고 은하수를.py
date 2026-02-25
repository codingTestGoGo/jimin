import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
dq = [deque([False] * 20) for _ in range(n)]

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

# set, tuple 사용 정답 1
# res = set()
# for i in range(n):
#     res.add(tuple(dq[i]))
# print(len(res))
    
# # set, tuple 사용 정답 2 - set을 {}로 바로 사용 가능
# print(len({tuple(dq[i]) for i in range(n)}))
print(len({tuple(x) for x in dq}))