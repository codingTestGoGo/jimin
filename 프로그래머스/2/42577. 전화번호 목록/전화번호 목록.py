def solution(phone_book):
    answer = True
    phone_book.sort()
    phone_dict = {num : True for num in phone_book} # {"119": True, "97674223": True, "1195524421": True} -> value는 의미 없음. for find 시간 복잡도 O(1)
    for num in phone_book:
        prefix = "" # 접두사
        for ch in num:
            prefix += ch
            if prefix in phone_dict and prefix != num: # 접두사 in 딕셔너리 and 본인 아님
                answer = False
                return answer
    return answer