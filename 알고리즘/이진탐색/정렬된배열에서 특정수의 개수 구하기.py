# N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어있음
# 이때 이 '수열에서 x가 등장하는 횟수를 계산하여라'
# ex) {1,1,2,2,2,2,3}에서 x=2이라면, 현재 수열에서 값이 2인 원소가 4개 이므로 4출력
# 단, 이문제는 시간복잡도 O(logN) 으로 알고리즘을 설계하지 않으면
# '시간초과' 판정을 받을 것 즉, 일반적인 '선형탐색'으로는 시간초과 판정
# 핵심 아이디어:
# '정렬된 데이터' 이고, O(logN)의 시간복잡도이기 때문에 '이진탐색'을 수행해야함
# 특정 값이 등장하는 첫번째 위치와 마지막 위치를 찾아, 위치 차이를 계산
# 즉 2번의 이진탐색을 진행해야함 ->첫번째 등장 위치와 마지막 등장 위치를 찾아야하니까
# 아니면 라이브러리를 활용해서 바로 사용가능!!!!!
# 7 2
# 1 1 2 2 2 2 3
from bisect import bisect_left, bisect_right
n, m = map(int, input().split())
arr = list(map(int, input().split()))


# 해당 range안의 데이서 갯수를 찾는 함수
def count_by_range(arr, left_val, right_val):
    left_idx = bisect_left(arr, left_val)
    right_idx = bisect_right(arr, right_val)
    return right_idx-left_idx


# 값이 [x,x]범위에 있는 데이터의 갯수 계산
count = count_by_range(arr, m, m)

# m이 해당 범위 내에 없다면 -1 출력
if count == 0:
    print(-1)
else:
    print(count)
