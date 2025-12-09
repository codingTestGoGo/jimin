import sys
input = sys.stdin.readline

n = int(input())

plus = [] # 양수 개수
minus = [] # 음수 개수
ones = 0 # 1 개수
zeros = 0 # 0 개수
for _ in range(n):
    num = int(input().strip())
    if num == 0:
        zeros += 1
    elif num == 1:
        ones += 1
    elif num > 1:
        plus.append(num)
    elif num < 0:
        minus.append(num)
plus.sort(reverse = True) # 양수는 내림차순 정렬
minus.sort()
# 양수 -> 큰 양수끼리 곱하기 (내림차순 정렬)
# 음수 -> 작은 음수(절대값 큰 음수)끼리 곱하기 (오름차순 정렬)
# 1 -> 더하기
# 0 -> 남은 음수 있으면 버리는 용도
ans = 0
for i in range(0, len(plus), 2):
    if i + 1 < len(plus): # 다음 원소 있는 경우 -> 곱해서 더하기
        ans += plus[i] * plus[i+1]
    else: # 다음 원소 없으면 그냥 더하기
        ans += plus[i]
for i in range(0, len(minus), 2):
    if i + 1 < len(minus):
        ans += minus[i] * minus[i+1]
    elif zeros: # 0 있으면 곱해서 없애기
        zeros -= 1
    else:
        ans += minus[i]
ans += ones

print(ans)