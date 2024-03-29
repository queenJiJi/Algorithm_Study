# 파이썬에서의 '큐'는 deque(덱) 라이브러리를 활용해서 사용
from collections import deque

# 큐(queue) 구현을 위해 deque 라이브러리 사용
queue = deque()

stack = []

# 삽입(5)-삽입(2)-삽입(3)-삽입(7)-삭제()-삽입(1)-삽입(4)-삭제()
queue.append(5)  # 5를 큐에 삽입
queue.append(2)  # 2를 큐에 삽입
queue.append(3)  # 3을 큐에 삽입
queue.append(7)  # 7을 큐에 삽입
queue.popleft()  # 삭제
queue.append(1)  # 1을 큐에 삽입
queue.append(4)  # 4를 큐에 삽입
queue.popleft()  # 삭제

print(queue)  # 먼저 들어온 순서대로 출력(선입선출)
queue.reverse()  # 역순으로 바꾸기
print(queue)  # 나중에 들어온 원소 부터 출력
