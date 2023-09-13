import math

def squareroot(Num):
    # Num이 제곱근일 경우
    if int(math.sqrt(Num)) == math.sqrt(Num):
        return 1
    #2개의 제곱근들의 합
    for i in range(1, int(math.sqrt(Num)) + 1):#0 부터 제곱근까지중에
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


'''
    cnt = 0
    MNum = Num
    n = int(pow(MNum, 1/2))  # 제곱근 구하기
    print("n : ",n)
    for i in range(n):
        Num = MNum
        i = n - i
        print("i : ",i)
        while(1):
            cnt += 1
            Nnum = Num - pow(i, 2)
            print("Num : ",Num)
            print("pow(i,2) : ",pow(i,2))
            print("Nnum : ",Nnum)

            if(Nnum == 0): #나머지 수가 0일 경우 스탑
                Nlist.append(cnt)
                print("cnt : ",cnt)
                print()
                break
            else: # 나머지 수가 있을 경우 제곱근 구하기
                Num = Nnum
                print("수정된 Num: ", Num)
                i = int(pow(Num, 1/2))
                print("바뀐 n : ",i)
    print(Nlist)
    return min(Nlist)


Num = int(input())
Nlist = []
count = squareroot(Num)
print(count)
'''