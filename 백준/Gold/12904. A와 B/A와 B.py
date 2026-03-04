import sys
input = sys.stdin.readline
from collections import deque

s = input().strip()
t = input().strip()

# t에서 역순으로 s 찾기
# 1. 문자열 뒤에서 A 제거
# 2. 문자열 뒤에서 B 제거하고 문자열 뒤집기
while len(t) > len(s):
    if t[-1] == 'A':
        t = t[:-1] # 'A' 제거
    else: # t[-1] == 'B'
        t = t[:-1][::-1] # 'B'제거 후 뒤집기
print(1 if s == t else 0)