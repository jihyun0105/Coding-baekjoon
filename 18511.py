Num, K = map(int, input().split())
cnt = 0
num = Num
while (num > 1):
    if num < 1:
        break
    else:
        num = num / 10
        cnt +=1

print(cnt)
print()
K_N = list(map(int, input().split()))
K_N = sorted(K_N,reverse=True)
print(K_N)

for i in range(cnt-1):
   Num = Num//10
print(Num)

max(K_N)

#중복순열 가장 큰수 계속 뽑아내고 작은 수 출력

