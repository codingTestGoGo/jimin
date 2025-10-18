import sys

n = int(input())
nums = sorted(list(map(int, sys.stdin.read().split())), reverse = True)
for num in nums:
    print(num)