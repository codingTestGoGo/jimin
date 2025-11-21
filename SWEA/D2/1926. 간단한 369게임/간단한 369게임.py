n = int(input())
nums = list(range(1, n + 1))
cond = ['3', '6', '9']
for num in nums:
    digits = list(str(num))
    flag = False
    for digit in digits:
        if digit in cond:
            print('-', end = '')
            flag = True
    if flag == False:
        print(num, end = '')
    print('', end = ' ')