import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
ans = 0
for num in a:
    ans += num*max(b)
    b.remove(max(b))
print(ans)