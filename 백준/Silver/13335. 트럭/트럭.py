import sys
from collections import deque
input = sys.stdin.readline

n, w, l = map(int, input().split()) # 트럭 수, 다리 길이, 최대하중
weights = list(map(int, input().split()))

q = deque()
q.append((weights[0], 0))
sum = weights[0]
time = 0
idx = 1

while q:
    time += 1

    if time - q[0][1] == w:
        sum -= q[0][0]
        q.popleft()

    if idx < n:
        if sum + weights[idx] > l or len(q) == w:
            continue
        else:
            q.append((weights[idx], time))
            sum += weights[idx]
            idx += 1
        
    if not q:
        print(time + 1)
        break
        