def solution(number,k):
  stack = [number[0]]
  # stack.append(number[0])

  for num in number[1:]:
    while stack and k>0 and stack[-1] < num:
      # if 
      stack.pop()
      k-=1
    stack.append(num)
  print(stack)
  if k!=0:
    stack=stack[:-k]
  return ''.join(stack)

print(solution('1924',2))
print(solution('1231234',3))
print(solution('4177252841',4))
