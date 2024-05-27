def solution(n,k):
  ans,result = [],[]
  def backtrack(start):
    if len(ans)==k:
      result.append(ans[:])
      return 
    
    for i in range(start,n+1):
      ans.append(i)
      backtrack(i+1)
      ans.pop()
    return result
  return backtrack(1)


print(solution(n = 4, k = 2))
print(solution(n = 1, k = 1))