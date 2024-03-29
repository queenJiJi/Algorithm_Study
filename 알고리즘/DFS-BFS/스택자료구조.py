# 파이썬에서의 '스택'은 리스트로 구현됨

stack = []

# 삽입(5)-삽입(2)-삽입(3)-삽입(7)-삭제()-삽입(1)-삽입(4)-삭제()
stack.append(5)  # 5를 스택에 삽입
stack.append(2)  # 2를 스택에 삽입
stack.append(3)  # 3을 스택에 삽입
stack.append(7)  # 7을 스택에 삽입
stack.pop()  # 삭제
stack.append(1)  # 1을 스택에 삽입
stack.append(4)  # 4를 스택에 삽입
stack.pop()  # 삭제

print(stack[::-1])  # 최상단 원소(가장 마지막에 들어온 것)부터 출력
print(stack)  # 최하단 원소(가장 처음 들어온 것)부터 출력
