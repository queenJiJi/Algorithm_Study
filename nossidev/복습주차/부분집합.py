# subsets
def solution(nums):
  ans,result =[],[]

  n = len(nums)

  def backtrack(start):
    result.append(ans[:])

    for i in range(start,n):
      ans.append(nums[i])
      backtrack(i+1)
      ans.pop()
    return result
  return backtrack(0)

print(solution([1,2,3]))