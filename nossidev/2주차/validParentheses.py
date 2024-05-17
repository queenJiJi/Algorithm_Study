def solution(s):
  stack =[]

  for i in s:
    if i=='(':
      stack.append(')')
    elif i=='[':
      stack.append(']')
    elif i == '{':
      stack.append('}')
    elif stack and stack[-1] == i:
      stack.pop()
    else:
      return False
  return False if stack else True


print(solution('()'))
print(solution('()[]{}'))
print(solution('(]'))
print(solution(']'))

