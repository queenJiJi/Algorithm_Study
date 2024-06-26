def solution(nums):
  n = len(nums)
  dp = [1] * n
  for i in range(1,n):
    for j in range(0,i):
      if nums[i] > nums[j]:
        dp[i] = max(dp[i], dp[j]+1)

  return max(dp)

print(solution([0,1,0,3,2,3]))
print(solution([7,7,7,7,7,7,7]))