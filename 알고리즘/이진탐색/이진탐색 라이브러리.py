# 파이썬 이진 탐색 라이브러리

# bisect_left(a,x) : 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환
# bisect_right(a,x) : 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스를 반환

# 간단 사용 방법
from bisect import bisect_left, bisect_right

# a = [1, 2, 4, 4, 8]
# x = 4

# print(bisect_left(a, x))
# print(bisect_right(a, x))


# 문제: 값이 특정 범위에 속하는 데이터 갯수 구하기

# 값이 [left_val, right_val]인 데이터의 갯수를 반환하는 함수
# 즉 해당 범위([left_val, right_val]) 안에 있는 데이터 갯수를 반환
# [-1,3]이라면 arr내에 -1이상 3이하인 데이터의 갯수를 구하는 것
def count_by_range(a, left_val, right_val):
    right_index = bisect_right(a, right_val)
    left_index = bisect_left(a, left_val)
    return right_index-left_index


# 배열 선언
a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# 값이 [4,4] 범위에 있는 데이터 갯수 출력 = 값이 4인 데이터 개수 출력
print(count_by_range(a, 4, 4))

# 값이 [-1,3] 범위에 있는 데이터 개수 출력
print(count_by_range(a, -1, 3))
