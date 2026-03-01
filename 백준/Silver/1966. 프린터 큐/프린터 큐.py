from collections import deque
import sys
input = sys.stdin.readline
tc = int(input().strip())

for _ in range(tc):
    n, m = map(int, input().split())
    q = deque()
    importances = list(map(int, input().split()))
    for i in range(n):
        q.append((i, importances[i]))
    order = 0
    flag = False
    while q:
        now_idx, now_imp = q.popleft()
        # 남은 것 중 더 큰 중요도가 있으면 뒤로 보냄
        if any(now_imp < imp for _, imp in q): 
            q.append((now_idx, now_imp))
            continue
        # 아니면 출력
        order += 1
        if now_idx == m:
            print(order)
            break
    