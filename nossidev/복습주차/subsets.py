def solution(nums):
  ans,result = [],[]
  
  def backtrack(start):
    result.append(ans[:])

    for i in range(start, len(nums)):
      ans.append(nums[i])
      backtrack(i+1)
      ans.pop()
    return result
  return backtrack(0)



print(solution(nums = [1,2,3]))
print(solution(nums = [0]))