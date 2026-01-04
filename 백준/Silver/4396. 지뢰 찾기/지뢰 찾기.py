import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0, -1, -1, 1, 1] 
dy = [0, 0, -1, 1, -1, 1, -1, 1] 

n = int(input())
grid1 = [list(input().strip()) for _ in range(n)]
grid2 = [list(input().strip()) for _ in range(n)]
ans = [['.' for _ in range(n)] for _ in range(n)]
is_mine = False


for i in range(n):
    for j in range(n):
        # grid2가 x(열림)이고 grid1이 .(지뢰없음)일 경우 -> 주변 지뢰 개수 확인 0~8
        cnt = 0
        if grid2[i][j] == 'x' and grid1[i][j] == '.':
            for k in range(8):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < n and 0 <= ny < n and grid1[nx][ny] == '*': # 지뢰 개수 세기
                    cnt += 1
            ans[i][j] = str(cnt)
                        
        # gird2가 x(열림)이고 grid1이 *(지뢰있음)일 경우 -> 지뢰 있는 모든 칸에 *표시
        elif grid2[i][j] == 'x' and grid1[i][j] == '*':
            is_mine = True

if is_mine == True:
    for i in range(n):
        for j in range(n):
            if grid1[i][j] == '*':
                ans[i][j] = '*'

for i in range(n):
    for j in range(n):
        print(ans[i][j], end = '')
    print()