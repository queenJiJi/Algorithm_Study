
from collections import deque

pair = {
    '(' : ')',
    '[' : ']',
    '{' : '}'
}

def check(s):
    st = []
    for e in s:
        if not st:
            st.append(e)
            continue
        if st[-1] in pair and pair[st[-1]] == e:
            st.pop()
        else:
            st.append(e)
    return not st

def solution(s):
    count = 0
    s = deque(s)
    for i in range(len(s)):
        if check(s):
            count += 1
        s.append(s.popleft())
    return count


print(solution("[](){}"))
print(solution("}]()[{"))
print(solution("[)(]"))
print(solution("}}}"))
