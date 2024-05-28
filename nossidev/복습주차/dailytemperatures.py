def solution(temperatures):
  temp = [[idx,val] for idx,val in enumerate(temperatures)]
  n = len(temp)
  ans = [0]*n
  stack = []

  for t in temp:
    while stack and stack[-1][1]<t[1]:
      ans[stack[-1][0]] = (t[0]-stack[-1][0])
      stack.pop()
    stack.append(t)

  return ans


print(solution([73,74,75,71,69,72,76,73]))
print(solution([30,40,50,60]))
print(solution([30,60,90]))