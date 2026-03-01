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
    order = 1
    flag = False
    while q:
        now_idx, now_imp = q.popleft()
        if not q:
            print(order)
            break
        for cmp_idx, cmp_imp in q:
            if now_imp < max(q, key = lambda x: x[1])[1]:
                q.append((now_idx, now_imp))
                break
            elif now_idx == m:
                print(order)
                flag = True
                break
            else:
                order += 1
                break
        if flag:
            break