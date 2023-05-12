import sys

N = int(input())  #피연산자의 개수
Sentence =(list(map(str, sys.stdin.readline().strip())))
Num = []
list = []

for _ in range(N):
    Num.append(int(sys.stdin.readline().strip()))

for i in Sentence:
    if i in ['+','-','*','/']:
        num2 = list.pop()
        num1 = list.pop()
        list.append(eval(f'{num1}{i}{num2}'))
    else:
        list.append(Num[ord(i)-ord('A')])

print(f'{list[0]:.2f}')



