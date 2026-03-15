import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [1] * n # i번째 원소를 마지막으로 하는 가장 긴 증가 부분 수열의 길이

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]: # 증가 수열 가능하면
            if dp[i] < dp[j] + 1: # 더 긴 길이로 갱신
                dp[i] = dp[j] + 1
print(max(dp))