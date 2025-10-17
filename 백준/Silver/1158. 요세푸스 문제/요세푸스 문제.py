n, k = map(int, input().split())
arr = list(range(1, n + 1))
idx = 0
print('<', end = '')
while(arr):
    idx = (idx + k - 1) % len(arr)
    if len(arr) == 1:
        print(arr.pop(idx), end = '>')
    else:
        print(arr.pop(idx), end = ', ')