def solution(s):
  stack = []

  for i in s:
    if i == '(':
      stack.append(')')
    elif i == '[':
      stack.append(']')
    elif i == '{':
      stack.append('}')
    elif stack and i == stack[-1]:
      stack.pop()
    else:
      return False
  return True if not stack else False




print(solution('()'))
print(solution('()[]{}'))
print(solution('(]'))
print(solution(']'))
