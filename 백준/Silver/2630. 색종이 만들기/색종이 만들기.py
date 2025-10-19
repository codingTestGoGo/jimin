import sys
input = sys.stdin.readline

n = int(input())
grid = list(input().split() for _ in range(n))

white = 0 # 잘라진 하얀 종이 개수
blue = 0 # 파란색 색종이의 개수
# print(*grid[0][0])
# exit()

def cut(x, y, size):
    global white, blue, grid
    
    # 현재 구역이 단색인지 확인
    first = grid[x][y] # 처음 색깔 저장
    same = True # 같은 지 확인 플래그
    for i in range(x, x + size):
        for j in range(y, y + size):
            if grid[i][j] != first:
                same = False
                break
        if not same:
            break
    # 단색이면 카운트하고 끝
    if same:
        if first == '0':
            white += 1
        else:
            blue += 1
        return
    # 아닐 경우 4등분 재귀
    half = size // 2
    cut(x, y, half)
    cut(x + half, y, half)
    cut(x, y + half, half)
    cut(x + half, y + half, half)

    
cut(0, 0, n)
print(white)
print(blue)