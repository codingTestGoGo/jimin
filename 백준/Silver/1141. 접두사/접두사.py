import sys
input = sys.stdin.readline

n = int(input())
arr = [input().strip() for _ in range(n)]
cnt_x = 0

# tc3 예외처리
arr = list(set(arr)) 
n = len(arr)

for i in range(len(arr)):
    for j in range(len(arr)):
        if i == j: # 자기자신
            continue
        if arr[i] == arr[j]: # 동일한 단어 -> 접두사 아님
            continue 
        if arr[j].find(arr[i]) == 0:
            cnt_x += 1
            break
print(n-cnt_x)
    
    