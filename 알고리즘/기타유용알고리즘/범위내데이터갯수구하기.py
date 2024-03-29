
# arr내에서 3-5(3,4,5)의 갯수를 구할때
# arr 내에서 하나(3)만의 갯수를 구하고 싶으면 3,3으로 범위를 두면 됨
from bisect import bisect_left, bisect_right

left, right = 3, 5
arr = [1, 2, 3, 3, 3, 4, 4, 5, 5, 6]


def count_by_range(arr, left_val, right_val):
    leftidx = bisect_left(arr, left_val)
    rightidx = bisect_right(arr, right_val)
    return rightidx-leftidx


count = count_by_range(arr, left, right)

if count == 0:
    print("해당 원소를 찾지 못했습니다")
else:
    print(count)
