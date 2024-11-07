def solution(a,b):

  result = []
  
  def backtrack(tmp,start):
    if len(tmp) == b:
      result.append(tmp[:])
      return
      
    for i in range(start,a+1):
      tmp.append(i)
      backtrack(tmp,i+1)
      tmp.pop()
  backtrack([], 1)
  return result

print(solution(3,1))
print(solution(4,2))
print(solution(4,4))