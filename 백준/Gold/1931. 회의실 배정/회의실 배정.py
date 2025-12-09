import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    start, end = map(int, input().split())
    arr.append((start, end))
# 끝나는 시간 빠른 기준으로 정렬, 끝나는 시간 동일할 경우 시작 시간 기준으로 정렬(시작=끝인 경우)
arr.sort(key = lambda x : (x[1], x[0])) # sort: 원본 변경
# arr = sorted(arr, key = lambda x : (x[1], x[0])) # sorted: 원본 유지

curr_end = 0
cnt = 0

for start, end in arr:
    if curr_end <= start:
        cnt += 1
        curr_end = end

print(cnt)