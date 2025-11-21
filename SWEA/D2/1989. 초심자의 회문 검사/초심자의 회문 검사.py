t = int(input())
for test_case in range(1, t + 1):
    print(f'#{test_case}', end = ' ')
    word = list(input().strip())
    reversed_word = word[::-1]
    if word != reversed_word:
        print(0)
    else: 
        print(1)
    
    # flag = True
    # for i in range(len(word)):
    #     # print(word[i], reversed_word[i])
    #     if word[i] != reversed_word[i]:
    #         flag = False
    #         break
    # if flag == False:
    #     print(0)
    # else:
    #     print(1)
