import sys

List=(list(map(str, sys.stdin.readline().strip())))
stack = []
count = 0
for i in range(len((List))):
    if List[i] == '(':  #'('를 만났을 경우
        stack.append(List[i])
    else: # ')'를 만났을 경우
        if List[i-1] == '(' and List[i] == ')' :  # ()모양이면 레이저임 
            stack.pop()
            count += len(stack) # '('의 개수만큼 조각이 생김
        else: # '))'를 만날경우 그 쇠막대기는 끝남 -> 조각 1개만 더 추가됨 
            stack.pop()
            count += 1
print(count)