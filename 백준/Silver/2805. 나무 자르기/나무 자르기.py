import sys

Num, Meter = map(int, input().split()) # 나무의 수, 집으로 가져가려는 나무의 길이
H_list = list(map(int,input().split()))  # 나무의 높이

start = 0
end =  max(H_list)
result = 0
while start <= end:
    meter = 0 # 현재 획득한 총 나무 길이
    mid = (start + end) // 2  # 나무의 높이를 합한 것을 절반으로 나눔
    for height in H_list: 
        if height > mid:
            meter += (height - mid)  #각 나무의 높이에서 절반을 뺌

    if meter >= Meter:  # 획득한 나무길이가 0이거나 원하는 길이보다 적을 떄
        result = mid
        start = mid + 1 # 중간값이 스타트값이 됨
    else: # meter > Meter # 중간값이 end값이 됨
        end = mid - 1

print(result) # 그 길이 프린트  