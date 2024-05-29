def solution(s):
  stack =[-1]
  answer =0

  for i in range(len(s)):
    if s[i] == '(':
      stack.append(i)
    else:
      stack.pop()
      if stack:
        answer=max(answer,i-stack[-1])
      else:
        stack.append(i)
  return answer

print(solution('(()'))
print(solution(')()())'))
print(solution(''))
print(solution('()(()'))