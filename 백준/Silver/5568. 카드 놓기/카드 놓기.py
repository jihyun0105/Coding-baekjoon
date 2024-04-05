from itertools import permutations

Card_N = int(input())   # 카드의 개수
Choice_K = int(input())  # 뽑는 카드의 개수
K_list = []
for i in range(Card_N):
        K_list.append(int(input()))
C_list =list(permutations(K_list,Choice_K)) # 뽑은 수 저장
Num = []
for i in C_list:
        Num.append(int(''.join(map(str,i))))

Num = list(set(Num))
print(len(Num))

