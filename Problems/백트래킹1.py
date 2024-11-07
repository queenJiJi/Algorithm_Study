def solution(a,b):

  result = []
  
  def backtrack(tmp):
    if len(tmp) == b:
      result.append(tmp[:])
      return
    
    for i in range(1,a+1):
      # if (tmp and tmp[-1] == i) or (i in tmp):
      #   continue

      if i not in tmp:
        tmp.append(i)
        backtrack(tmp)
        tmp.pop()
   
  backtrack([])
  result.sort()
  return [i for i in result]


print(solution(3,1))
print(solution(4,2))
print(solution(4,4))