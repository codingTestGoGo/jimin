import sys

input = sys.stdin.readline

n = int(input())

# dp[i][0] = i행 사자 x
# dp[i][1] = i행 왼쪽 칸에만 사자
# dp[i][2] = i행 오른쪽 칸에만 사자
dp = [[0, 0, 0] for _ in range(n + 1)]

dp[1][0] = 1
dp[1][1] = 1
dp[1][2] = 1

for i in range(2, n + 1):
    # 이번 행  -> 이전 행 상관x
    dp[i][0] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]) % 9901

    # 이번 행 쪽에 o -> 이전 행 세로 인접 x
    dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % 9901

    # 이번 행 오른쪽 o -> 이전 행 세로 인접 x
    dp[i][2] = (dp[i - 1][0] + dp[i - 1][1]) % 9901

print(sum(dp[n]) % 9901)