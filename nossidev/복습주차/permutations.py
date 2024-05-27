def solution(nums):
  ans,result =[],[]
  n = len(nums)
  def backtrack():
    if n == len(ans):
      result.append(ans[:])
      return
    
    for i in range(n):
      if nums[i] not in ans:
        ans.append(nums[i])
        backtrack()
        ans.pop()
    return result
  return backtrack()
  
print(solution(nums = [1,2,3]))
print()
print(solution(nums = [0,1]))
print()
print(solution(nums = [1]))