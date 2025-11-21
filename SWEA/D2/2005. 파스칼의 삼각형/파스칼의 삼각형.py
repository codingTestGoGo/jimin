t = int(input())
for test_case in range(1, t + 1):
    print(f'#{test_case}')
    n = int(input())
    arr = [[] for _ in range(n)]
    for i in range(len(arr)):
        for j in range(i + 1):
            arr[i].append(1)
    for i in range(1, n):
        for j in range(1, i):
            arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]
    for row in arr:
        print(*row)
            