from collections import deque

# 스택 풀이


def split_string_stack(w):
    stack = []
    for i in w:
        if i == '(':
            stack.append(i)
        else:  # i==')'
            if stack == []:  # 처음으로 ')' 부터 들어왔을 시
                return False
            else:  # stack이 비어있지 않다면
                stack.pop()  # '(' 하나 제거
    return stack == []  # stack이 완전히 비어있으면 True아니면 False 반환

# 큐 풀이


def split_string_q(w):
    q = deque(w)
    answer = []
    while q:
        item = q.pop()
        if item == '(':
            answer.append(item)
        else:
            if answer == []:
                return False
            else:
                if item == ')':
                    answer.remove('(')
    return answer == []


# 쉬운 풀이
def solution(w):
    count = 0
    for i in w:
        if i == '(':
            count += 1
        else:  # i==')'
            if count > 0:  # count가 빈 상태가 아니라면
                count -= 1  # 빼주고
    #         else:  # count ==0 or count <0 # count가 빈상태이거나 '('가 이미 있는데 또 '('라면
    #             return False
    # if count > 0: #count가 0이상이라면
    #     return False
    return True if count == 0 else False


print(solution('()()'))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))
print()
print(split_string_stack('()()'))
print(split_string_stack("(())()"))
print(split_string_stack(")()("))
print(split_string_stack("(()("))
print()
print(split_string_q('()()'))
print(split_string_q("(())()"))
print(split_string_q(")()("))
print(split_string_q("(()("))
