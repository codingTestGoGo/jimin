T = int(input())
for test_case in range(1, T + 1):
    print(f'#{test_case}', end = ' ')
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]

    max_sum = 0
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            x, y = 0, 0
            tmp_sum = 0
            for x in range(i, i + m):
                tmp_sum += sum(grid[x][j : j + m])
            if tmp_sum > max_sum:
                max_sum = tmp_sum
    print(max_sum)