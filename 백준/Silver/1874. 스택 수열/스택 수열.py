import sys
input = sys.stdin.readline

n = int(input())
st = []
res = []
cnt = 1
for i in range(n):
    num = int(input()) 
    while cnt <= num:
            st.append(cnt)
            res.append('+')
            cnt += 1
    if st[-1] == num and len(st) != 0:
        st.pop()
        res.append('-')
    else:
        print("NO")
        exit()

print('\n'.join(res))