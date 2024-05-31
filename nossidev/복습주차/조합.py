# combinations 
def solution(nums,k):
  ans, result = [],[]
  n = len(nums)
  def backtrack(start,k):
    
    if len(ans) == k:
        result.append(ans[:])
        return
    for i in range(start,n):
      ans.append(nums[i])
      backtrack(i+1,k)
      ans.pop()

    return result
  return backtrack(0,k)

print(solution(nums= [1,2,3,4],k=2))