import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
dx = [-1, 1, 0, 0] # 상하좌우(행)
dy = [0, 0, -1, 1] # 상하좌우(열)
for _ in range(n):
    w, h = map(int, input().split())
    grid = [list(input().strip()) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    sec = 0
    q_road = deque([])
    q_fire = deque([])
    is_possible = False
    is_escaped = False
    for i in range(h):
        for j in range(w):
            if grid[i][j] == '@':
                if i == 0 or i == h - 1 or j == 0 or j == w - 1: # 시작이 가장자리인 경우 즉시 탈출 
                    print(1)
                    is_escaped = True
                    break
                q_road.append((i, j))
                visited[i][j] = True
                grid[i][j] = '.' # 불 번질 수 있는 좌표 표시 용도
                
            elif grid[i][j] == '*':
                q_fire.append((i, j))
        if is_escaped == True:
            break
    if is_escaped == True:
        continue
    while(q_road):
        sec += 1
        len_q_fire = len(q_fire)
        for _ in range(len_q_fire): # 아직 번질 불 남아있을 때  
            fire_x, fire_y = q_fire.popleft()
            for k in range(4):
                fire_nx = fire_x + dx[k]
                fire_ny = fire_y + dy[k]
                if 0 <= fire_nx < h and 0 <= fire_ny < w and grid[fire_nx][fire_ny] == '.': # 빈 공간
                    grid[fire_nx][fire_ny] = '*'
                    q_fire.append((fire_nx,fire_ny))
        len_q_road = len(q_road)
        for _ in range(len_q_road):
            road_x, road_y = q_road.popleft()
            for k in range(4):
                road_nx = road_x + dx[k]
                road_ny = road_y + dy[k]
                if (road_nx < 0 or road_nx >= h or road_ny < 0 or road_ny >= w): # 탈출 조건
                        print(sec)
                        is_possible = True
                        is_escaped = True
                        break
                if 0 <= road_nx < h and 0 <= road_ny < w  and grid[road_nx][road_ny] == '.' and not visited[road_nx][road_ny]: # 빈 공간
                    q_road.append((road_nx, road_ny))
                    visited[road_nx][road_ny] = True
            if is_escaped: break
        if is_escaped: break
    if is_escaped: continue

    if not is_possible: print('IMPOSSIBLE')
                                