N, K_len = map(int, input().split())
K = list(map(int, input().split()))
K.sort(reverse=True)  #내림차순

def find_largest_num(N, K):
    #N의 자릿수 계산
    N_str = str(N)     #문자로 변경한 후
    N_len = len(N_str)     #자릿수 계산
    
    for length in range(N_len, 0, -1):
        candidates = []

        #dfs 함수        
        def dfs(start_idx, constructed_num):   #깊이 우선 탐색
            if len(constructed_num) == length:
                candidates.append(int(constructed_num))
                return
            
            #숫자 조합 검사
            for k_num in K:
                if constructed_num == '' and k_num == 0:
                    continue
                
                new_num = constructed_num + str(k_num)
                if int(new_num + '0' * (length - len(new_num))) <= N:
                    dfs(start_idx + 1, new_num)
        
        dfs(0, '')
        #결과 반환
        if candidates:
            return max(filter(lambda x: x <= N, candidates))

print(find_largest_num(N, K))