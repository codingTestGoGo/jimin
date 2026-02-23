import sys
input = sys.stdin.readline

q_idx = 0
u_idx = 0
a_idx = 0
c_idx = 0
k_idx = 0

# arr = list(input())
arr = input().strip()
res = 0
idle = 0 # 재사용 가능한 오리 수 
for ch in arr:
    if ch == 'q':
        if idle > 0:
            idle -= 1 # 끝난 오리 재사용
        else:
            res += 1
        q_idx += 1
    elif ch == 'u':
        if q_idx <= u_idx :
            print(-1)
            exit(0)
        u_idx += 1
    elif ch == 'a':
        if u_idx <= a_idx :
            print(-1)
            exit(0)
        a_idx += 1  
    elif ch == 'c':
        if a_idx <= c_idx :
            print(-1)
            exit(0)
        c_idx += 1
    elif ch == 'k':
        if q_idx < 1 or u_idx < 1 or a_idx < 1 or c_idx < 1:
            print(-1)
            exit(0)
        # quack 완료 처리
        q_idx -= 1
        u_idx -= 1
        a_idx -= 1
        c_idx -= 1
        idle += 1
         
    else:
        print(-1)
        exit(0)

# 중간에 끊긴 오리
if q_idx != 0 or u_idx != 0 or a_idx != 0 or c_idx != 0:
    print(-1)
else:
    print(res)