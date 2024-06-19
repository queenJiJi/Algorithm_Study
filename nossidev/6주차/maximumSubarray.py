def solution(nums):
  n = len(nums)
  dp = [0]*n

  dp[0] = nums[0]

  for i in range(1,n):
    dp[i] = max(dp[i-1]+nums[i], nums[i])
  return max(dp)

print(solution([-2,1,-3,4,-1,2,1,-5,4]))
print(solution([1]))
print(solution([5,4,-1,7,8]))