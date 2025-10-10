import sys
input = sys.stdin.readline
k = int(input())
st = []
sum = 0
for _ in range(k):
    num = int(input())
    if num == 0:
        st.pop()
    else:
        st.append(num)

for _ in range(len(st)):
    sum += st.pop()
print(sum)
