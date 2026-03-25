import sys
input = sys.stdin.readline

arr = input().strip().split('-')
res = 0

if arr[0] == '':
    if '+' in arr[1]:
        tmp = arr[1].split('+')
        arr[1] = -int(tmp[0]) + int(tmp[1])
    else: 
        arr[1] = -int(arr[1])
    del(arr[0])

for i in range(len(arr)):
    if len(arr) == 1:
        if type(arr[i]) == int and arr[i] < 0:
            res += arr[i]
            break
        res += sum(map(int, str(arr[i]).split('+')))
        break   

    if i == 0:
        if type(arr[i]) == int:
            res += arr[i]
        elif '+' in arr[i]:
            res += sum(map(int, arr[i].split('+')))
        else:
            res += int(arr[i])
    else:
        if '+' in str(arr[i]):
            res -= sum(map(int, str(arr[i]).split('+')))
        else:
            res -= int(arr[i])

print(res)