# 키보드에서 5개의 정수를 입력 받아 리스트에 저장하고 평균을 구하는 프로그램을 작성하시오
a = []
_sum = 0;
for i in range(0, 5):
    n = int(input('> '))
    a.append(n)
    _sum += n
print('평균', _sum / 5.00, sep=':')
print(a)
