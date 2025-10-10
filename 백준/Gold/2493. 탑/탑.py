import sys
input = sys.stdin.readline

n = int(input())
heights = list(map(int, input().split())) # 초기 탑 높이 저장

st = [] # 처리 전 탑 (인덱스, 높이)
res = [] # 결과 저장용

for i in range(n):
    now_height = heights[i]

    while len(st) != 0 and st[-1][1] < now_height:
        st.pop()

    if len(st) == 0:
        res.append(0)
    else:
        res.append(st[-1][0])
    st.append((i + 1, now_height))
        
print(*res)