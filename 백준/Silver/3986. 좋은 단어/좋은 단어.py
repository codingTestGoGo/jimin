import sys
input = sys.stdin.readline
cnt = 0

n = int(input())
for _ in range(n):
    s = list(input().strip())
    st = []
    for ch in s:
        if not st:
            st.append(ch)
        elif st[-1] == ch:
            st.pop()
        else:
            st.append(ch)
    if not st:
        cnt += 1
print(cnt)