import sys

N = int(input())  # 탑의 수를 나타내는 정수 N

height = list(map(int, sys.stdin.readline().split()))  # N개의 탑들의 높이를 리스트로 저장5
ans = [0 for i in range(N)] # 탑의 수만큼 0을 채운다.
stack = []  # 높이 ,  index

for i in range(N):  # 자신보다 작은 타워는 앞으로도 쓸 일 X
    while stack:
        if stack[len(stack)-1][0] > height[i] :  # 다음 탑의 높이보다 스택의 top이 더 큰 경우 → 신호 수신 가능
            ans[i] = stack[len(stack)-1][1] + 1
            break
        else:    #스택의 top보다 다음 탑의 높이가 더 큰 경우
            stack.pop()
    stack.append([height[i],i])
print(*ans)