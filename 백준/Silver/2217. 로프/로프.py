import sys
input = sys.stdin.readline

n = int(input())
w = []
for _ in range(n):
    w.append(int(input().strip()))
w.sort() # 오름차순 정렬
# 10 15
# k=1개 선택 -> 15*1 = 30 // w[1]*2 = w[n-k]*k
# k=2개 선택 -> 10*2 = 20 // w[0]*2 = w[n-k]*k
ans = 0
for k in range(1,n+1):
    ans = max(ans, w[n-k]*k)
print(ans)