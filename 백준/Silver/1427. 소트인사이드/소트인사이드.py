import sys
from math import gcd

num = list(input())
num = sorted(num, reverse = True)
print(''.join(num))
# print(*num, sep = '')

