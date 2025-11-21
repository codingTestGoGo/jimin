t = int(input())
for test_case in range(1, t + 1):
    print(f'#{test_case}', end = ' ')
    grid = [list(map(int, input().split())) for _ in range(9)]
    flag = True

    # 3x3 check
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            box = []
            for x in range(i, i + 3):
                for y in range(j, j + 3):
                    box.append(grid[x][y])
            if set(box) != set(range(1, 10)):
                flag = False

    # row check
    for row in grid:
        if set(row) != set(range(1, 10)):
            flag = False

    # col check
    for row in range(9):
        col_arr = []
        for col in range(9):
            col_arr.append(grid[col][row])
        if set(col_arr) != set(range(1, 10)):
            flag = False

    if flag:
        print(1)
    else:
        print(0)