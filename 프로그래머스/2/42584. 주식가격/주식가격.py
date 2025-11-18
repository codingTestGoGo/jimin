def solution(prices):
    answer = [0] * len(prices)
    st = [] # 가격이 떨어지지 않고 있는 인덱스 저장
    for i in range(len(prices)):
        while st and prices[i] < prices[st[-1]]: #  현재 가격 < 스택 탑 가격
            top = st.pop()
            answer[top] = i - top 
        st.append(i)
    while st:
        answer[st[-1]] = len(prices) - st[-1] -1
        st.pop()
    return answer