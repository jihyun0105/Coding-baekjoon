import collections
from collections import deque

N = int(input())
Num = deque()
for i in range (N):
    Num.append(i+1)

while N != 1:
    Num.popleft()
    N = N-1
    Num.insert(N+1,Num[0])
    Num.popleft()

print(Num[0])

