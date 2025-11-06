# ASCII A:65 a:97
# ord(): str to unicode
def solution(myString):
    answer = ''
    for i in range(len(myString)):
        if ord(myString[i]) >= ord('a'):
            answer += (chr(ord(myString[i]) - (ord('a') - ord('A'))))
        else:
            answer += (myString[i])

    return answer