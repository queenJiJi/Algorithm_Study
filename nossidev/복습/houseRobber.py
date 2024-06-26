def solution(nums):
  n = len(nums)
  dp=[0]*n

  dp[0] = nums[0]
  dp[1] = max(nums[0],nums[1])

  for i in range(2,n):
    dp[i] = max(dp[i-2]+nums[i], dp[i-1])
  return dp[n-1]

print(solution([1,2,3,1]))
print(solution([2,7,9,3,1]))