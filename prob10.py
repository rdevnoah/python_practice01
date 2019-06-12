# 숫자를 입력 받아서 아래와 같은 실행결과가 나타나도록 코드를 완성하세요.


num = int(input('숫자를 입력하세요: '))


def f(count, start):
    result = start;
    for i in range(0, count-1):
        start += 2
        result += start
    print(result)


f(num // 2, 2) if num % 2 == 0 else f((num + 1) // 2, 1)

