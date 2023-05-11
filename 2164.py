N = int(input())
Num = []
for i in range (N):
    Num.append(i+1)

while N != 1:
    Num.pop(0)
    N = N-1
    Num.insert(N+1,Num[0])
    Num.pop(0)

print(Num)

