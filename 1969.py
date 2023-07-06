import sys

DNA_N, DNA_M = map(int, sys.stdin.readline().split()) #DNA_N= DNA수, DNA_M = 문자열 길이
DNA_L1 = [] #DNA를 담을 리스트
DNA_L1 = [sys.stdin.readline().strip() for _ in range(DNA_N)]

DNA_L2 = [] #Hamming Distance의 합이 가장 작은 DNA
for i in range(DNA_M):
        cnt = [0, 0, 0, 0] # A,C,G,T순
        # DNA중에서 가장 많이 나온 뉴클레오티드 구함
        for j in range(DNA_N):
            if DNA_L1[j][i] == 'A':
                cnt[0] += 1
            elif DNA_L1[j][i] == 'C':
                cnt[1] += 1
            elif DNA_L1[j][i] == 'G':
                cnt[2] += 1
            elif DNA_L1[j][i] == 'T':
                cnt[3] += 1

        id = cnt.index(max(cnt)) # 값이 가장 큰 cnt의 인덱스 번호를 가져옴
        if id == 0:
            DNA_L2.append('A')
        elif id == 1:
            DNA_L2.append('C')
        elif id == 2:
            DNA_L2.append('G')
        else:
            DNA_L2.append('T')

H_D = 0  #Hamming Distance의 합
for i in range(DNA_N):
    for j in range(DNA_M):
        if DNA_L2[j] != DNA_L1[i][j]:
            H_D += 1


print(''.join(DNA_L2))
print(H_D)



