def parse(w):  # 올바른 문자열까지인지 아닌지와 아닌 곳부터의 위치 반환 함수
    left, right = 0, 0  # '('의 갯수 left, ')'의 갯수 right
    flag = True
    stack = []
    for i in range(len(w)):
        if w[i] == '(':
            left += 1
            stack.append(w[i])
        else:
            right += 1
            if len(stack) == 0:
                flag = False
            else:
                stack.pop()
        if left == right:
            return flag, i+1
    return False, 0


def solution(p):
    answer = ''
    if p == '':  # 1
        return p
    correct, pos = parse(p)  # 2
    u = p[:pos]
    v = p[pos:]

    if correct == True:  # 3
        return u+solution(v)  # 3-1
    else:  # 4
        answer = '('+solution(v)+')'  # 4-1,4-2,4-3
        for i in range(1, len(u)-1):  # 4-4
            if u[i] == '(':
                answer += ')'
            else:
                answer += '('
        return answer  # 4-5
