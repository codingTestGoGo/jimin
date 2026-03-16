import sys
input = sys.stdin.readline
arr = input().strip()

st = []
check = []
check_flag = False
for w in arr:
    if w == '(':

        if st and (st[-1] == '2' or st[-1] == '3' or st[-1] == ')') :
            st.append('+')
        st.append('2')
        st.append('*')
        st.append('(')
        
        check.append(w)

    elif w == ')':
        flag = False

        while st and (st[-1] == '*' or st[-1] == '('):
            flag = True
            st.pop()
        if not flag:
            st.append(')')
            
        if not check or check[-1] != '(':
            check_flag = True
            break
        else:
            check.pop()

    elif w == '[':
        if st and (st[-1] == '2' or st[-1] == '3' or st[-1] == ')'):
            st.append('+')
        st.append('3')
        st.append('*')
        st.append('(')
        
        check.append(w)

    elif w == ']':
        flag = False

        while st and (st[-1] == '*' or st[-1] == '('):
            flag = True
            st.pop()
        if not flag:
            st.append(')')
            
        if not check or check[-1] != '[':
            check_flag = True
            break
        else:
            check.pop()

if check_flag or check:
    print(0)
else: 
    expr = ''.join(st)
    result = eval(expr)
    print(result)