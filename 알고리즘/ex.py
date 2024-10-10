from collections import deque

col, row = 3, 3
board = [[j * col + i for i in range(1, col + 1)] for j in range(row)]

# board 출력 (변경 전)
print("Before:")
for i in board:
    print(*i)

# 각 열의 값을 deque로 나누어 저장
left, mid, right = deque(), deque(), deque()
left.extend([1, 4, 7])
mid.extend([2, 5, 8])
right.extend([3, 6, 9])

# 요소들을 한 칸씩 순환시킴
tmp = left.popleft()    # 왼쪽 첫 번째 열의 값들 [1, 4, 7]을 pop
mid.append(tmp)         # 이 값을 mid에 추가

tmp = mid.pop()         # mid의 마지막 값을 pop
right.appendleft(tmp)   # 이를 right의 앞에 추가

tmp = right.pop()       # right의 마지막 값을 pop
mid[-1] = tmp           # 이를 mid의 마지막 요소로 교체

tmp = mid.popleft()     # mid의 첫 번째 값을 pop
left.append(tmp)        # 이를 left에 추가

# 결과적으로 순환된 값들을 다시 board로 복원
board = [
    [left[0], mid[0], right[0]],
    [left[1], mid[1], right[1]],
    [left[2], mid[2], right[2]],
]

# board 출력 (변경 후)
print("\nAfter:")
for i in board:
    print(*i)