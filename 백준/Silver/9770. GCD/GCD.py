import sys
from math import gcd

nums = list(map(int, sys.stdin.read().split()))
ans = 0
n = len(nums)

for i in range(n):
    for j in range(i + 1, n):
        ans = max(ans, gcd(nums[i], nums[j]))

print(ans)
