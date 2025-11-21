T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    print(f'#{test_case}', end = ' ')
    sum = 0
    max_price = 0
    for price in reversed(arr):
        if price > max_price:
            max_price = price
        else:
            sum += max_price - price
    print(sum)
