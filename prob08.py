# 문자열을 입력 받아, 해당 문자열을 문자 순서를 뒤집어서 반환하는 함수 reverse(s)을 작성하세요.


s = input('입력>')


def reverse(s):
    length = len(s)
    result = ''
    for i in range(0, length):
        result += s[length-1-i]
    return result


print('결과',reverse(s),sep='>')
