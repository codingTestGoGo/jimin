import sys
# from collections import deque
input = sys.stdin.readline

n = int(input())
flowers = []

for _ in range(n):
    sm, sd, em, ed = map(int, input().split())
    start = sm * 100 + sd
    end = em * 100 + ed
    flowers.append((start, end))
# print(flowers)
flowers.sort()
# print(flowers)
cur = 301 # 3월 1일
target = 1201 # 12월 1일
i = 0 # pointer
ans = 0
best_end = cur

# greedy: cur 이전에 시작하는 꽃들 중 end가 가장 뒤인 것 고름
while cur < target:
    updated = False
    while i < n and flowers[i][0] <= cur:
        if flowers[i][1] > best_end:
            best_end = flowers[i][1]
            updated = True
        i += 1
    
    # 탈출 조건
    if not updated:
        ans = 0
        break

    # 하나 선택 후 cur 확장
    cur = best_end
    ans += 1

print(ans)