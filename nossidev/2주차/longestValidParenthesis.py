def solution(s):
  stack =[-1] 
  answer = 0

  for i in range(len(s)):
    if s[i]=='(': 
      stack.append(i)
    else: # s[i] == ')'
      stack.pop()
      if stack: # 스택이 비어있지 않다면
        answer = max(answer,(i-(stack[-1])))
      else: # 스택이 비어있다면
        stack.append((i))
  return answer

print(solution('(()'))
print(solution(')()())'))
print(solution(''))
print(solution('()(()'))
print(solution('()'))

