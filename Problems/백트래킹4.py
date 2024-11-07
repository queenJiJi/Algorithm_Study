def solution(a,b):
  result = []

  def backtrack(tmp):
    if len(tmp) == b:
      result.append(tmp[:])
      return
    
    for i in range(1,a+1):
      if tmp and i < tmp[-1]:
        continue
      tmp.append(i)
      backtrack(tmp)
      tmp.pop()

  backtrack([])
  return result

print(solution(4,2))
print(solution(3,3))