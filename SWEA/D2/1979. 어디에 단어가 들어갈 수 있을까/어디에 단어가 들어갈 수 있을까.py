t = int(input())
for test_case in range(1, t + 1):
    print(f'#{test_case}', end = ' ')
    n, k = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]

    cnt = 0
    ans = [1] * k
    # row
    for row in grid:
        for i in range(n - k + 1):
            if row[i:i+k] == ans :
                # 오른쪽 끝이면 범위 왼쪽 부분이 1이 아니어야 함, 왼쪽 끝일 경우도 마찬가지, 양끝이 아닌 경우도 범위 외는 1 아니어야 함
                if (i+k == n and row[i - 1] != 1) or (i == 0 and row[i+k] != 1) or (i+k != n and i != 0 and row[i - 1] != 1 and row[i+k] != 1):
                    cnt += 1

    # col
    for row in range(n):
        tmp = []
        for col in range(n):
            tmp.append(grid[col][row])
        for i in range(n - k + 1):
            if tmp[i:i+k] == ans :
                # 오른쪽 끝이면 범위 왼쪽 부분이 1이 아니어야 함, 왼쪽 끝일 경우도 마찬가지, 양끝이 아닌 경우도 범위 외는 1 아니어야 함
                if (i+k == n and tmp[i - 1] != 1) or (i == 0 and tmp[i+k] != 1) or (i+k != n and i != 0 and tmp[i - 1] != 1 and tmp[i+k] != 1):
                    cnt += 1
    print(cnt)