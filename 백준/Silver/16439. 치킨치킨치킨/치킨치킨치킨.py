from itertools import combinations
P_N, C_N = map(int, input().split()) #P_N = 고리 회원수, C_N= 치킨 종류의 수

Favorite = [list(map(int,input().split())) for _ in range(P_N)]


max_F = 0
for a, b, c in combinations(range(C_N),3): #치킨 종류에서 조합을 이용해 3개 고름
    F_Sum = 0
    for i in range((P_N)):
        F_Sum += max(Favorite[i][a], Favorite[i][b], Favorite[i][c]) #3종류의 치킨중 가장 선호도가 높은 것을 더한 값
    max_F = max(max_F,F_Sum) #선호도를 더한 값 중 가장 큰 값
print(max_F)