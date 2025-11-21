t = int(input())
for test_case in range(1, t + 1):
    print(f'#{test_case}', end = ' ')
    n = int(input())
    arr = list(map(int, input().split()))
    print(*sorted(arr))