import math

def squareroot(Num):
    # Num이 제곱근일 경우
    if int(math.sqrt(Num)) == math.sqrt(Num):
        return 1
    #2개의 제곱근들의 합
    for i in range(1, int(math.sqrt(Num)) + 1):#0부터 제곱근까지중에
        if int(math.sqrt(Num - i ** 2)) == math.sqrt(Num - i ** 2):#원래 값에서 i**2을 뺀게 정수이면
            return 2

    #3개의 제곱근들의 합
    for i in range(1, int(math.sqrt(Num)) + 1):
        for j in range(1, int(math.sqrt(Num - i ** 2)) + 1):
            if int(math.sqrt(Num - i ** 2 - j ** 2)) == math.sqrt(Num - i ** 2 - j ** 2):
                return 3

    # 그 이외의 것
    return 4

Num = int(input())
print(squareroot(Num))