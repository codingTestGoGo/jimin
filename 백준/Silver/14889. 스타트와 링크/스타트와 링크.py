import sys
input = sys.stdin.readline
from itertools import permutations, combinations

n = int(input())
grid = [[0] * n for _ in range(n)]
for i in range(n):
    grid[i] = (list(map(int, input().split())))
arr = [i for i in range(n)]
perm = combinations(arr, n//2)
res = 99999 # 팀별 능력치 차이 최소값 저장
for val in perm:
    team_a = []
    team_b = []
    for i in range(n//2):
        team_a.append(val[i])
    team_b = [x for x in arr if x not in team_a]
    comb_a = list(combinations(team_a, 2))
    comb_b = list(combinations(team_b, 2))

    sum_a, sum_b = 0, 0
    for val_a in comb_a:
        
        i = val_a[0]
        j = val_a[1]
        sum_a += grid[i][j]
        sum_a += grid[j][i]
    
    for val_b in comb_b:
        
        i = val_b[0]
        j = val_b[1]
        sum_b += grid[i][j] 
        sum_b += grid[j][i] 
    
    res = min(res, abs(sum_a - sum_b))
print(res) 