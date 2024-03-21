N = int(input()) 
work = [list(map(int, input().split())) for _ in range(N)] 
dp = [0] * (N + 1) 
for i in range(N):
    time, pay = work[i] 
    if i + time <= N:
        dp[i + time] = max(dp[i + time], dp[i] + pay) 
    dp[i + 1] = max(dp[i + 1], dp[i])  

print(dp[N])  
