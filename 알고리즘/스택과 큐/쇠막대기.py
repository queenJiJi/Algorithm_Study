ex = input()
stack = []
ans = 0

for i in range(len(ex)):
    if ex[i] == '(':
        stack.append(ex[i])
    else: #')'
        if ex[i-1] == ')': # 막대기
            stack.pop()
            ans += 1
        elif ex[i-1] == '(': # 레이저
            stack.pop()
            ans += len(stack) # 막대갯수 카운팅
print(ans)
