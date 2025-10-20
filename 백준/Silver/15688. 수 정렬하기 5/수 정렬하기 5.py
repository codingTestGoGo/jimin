import sys

n = int(input())
nums = sorted(list(map(int, sys.stdin.read().split())))

for num in nums:
    print(num)
