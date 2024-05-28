def solution(s):
  stack = []
  for ch in s:
    if ch =='(':
      stack.append(')')
    elif ch == '{':
      stack.append('}')
    elif ch == '[':
      stack.append(']')
    else:
      if stack and ch == stack[-1]:
        stack.pop()
  return False if stack else True


print(solution(s = "()"))
print(solution(s = "()[]{}"))
print(solution(s = "(]"))
