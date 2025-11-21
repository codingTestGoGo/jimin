t = int(input())
for test_case in range(1, t + 1):
    print(f'#{test_case}', end = ' ')
    words = list(str(input()))
    # size = 1
    flag = False
    for size in range(1, len(words)):
        if flag == True:
            break
        for i in range(0, len(words) - size, size):
            if words[i:i+size] != words[i+size:i+size*2]:
                break
            else: 
                print(len(words[i:i+size]))
                flag = True
                break