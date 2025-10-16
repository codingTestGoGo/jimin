import sys

n, k = map(int, input().split())
coins = reversed(list(map(int, sys.stdin.read().split())))
ans = 0
for coin in coins:
    ans += k // coin
    k %= coin

print(ans)