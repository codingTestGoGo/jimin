import sys
input = sys.stdin.readline

n = int(input())
res = 0
arr = []
for _ in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))
arr.sort()
start = arr[0][0]
end = arr[0][1]
for x, y in arr[1:]:
    if x <= end: # 겹치거나 닿을 경우 합치기
        if y > end:
            end = y
    else:
        res += end - start
        start = x
        end = y
res += end - start   
print(res)