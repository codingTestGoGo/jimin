import sys
input = sys.stdin.readline

# 계단 개수 입력
n = int(input())

# stairs[i] = i번째 계단의 점수
# 1번 인덱스부터 쓰기 위해 맨 앞에 0을 하나 넣어 둔다.
stairs = [0]

for _ in range(n):
    stairs.append(int(input()))

# 계단이 1개뿐이면, 그 계단을 밟는 것이 정답
if n == 1:
    print(stairs[1])

# 계단이 2개면, 둘 다 밟는 것이 최대 점수
elif n == 2:
    print(stairs[1] + stairs[2])

else:
    # dp[i] = i번째 계단을 반드시 밟았을 때 얻을 수 있는 최대 점수
    dp = [0] * (n + 1)

    # 초기값 설정
    dp[1] = stairs[1]
    dp[2] = stairs[1] + stairs[2]
    dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

    # 4번째 계단부터 점화식 적용
    for i in range(4, n + 1):
        # 방법 1: i-2 -> i
        case1 = dp[i - 2] + stairs[i]

        # 방법 2: i-3 -> i-1 -> i
        case2 = dp[i - 3] + stairs[i - 1] + stairs[i]

        dp[i] = max(case1, case2)

    # 마지막 계단은 반드시 밟아야 하므로 dp[n]이 정답
    print(dp[n])