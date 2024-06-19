def solution(nums):
  n = len(nums)
  # top-down
  # memo = {}
  # def dp(n):
  #   if n==0:
  #     return nums[0]
  #   if n==1:
  #     return max(nums[0], nums[1])
    
  #   if n not in memo:
  #     memo[n] = max(dp(n-2)+nums[n], dp(n-1))
  #   return memo[n]
  # return dp(n-1)

  # # bottom-up
  # dp = [-1]* n

  # dp[0] = nums[0]

  # if n>1: # nums의 길이가 1이하일땐 out of index 뜨기 때문에 예외처리
  #   dp[1] = max(nums[0],nums[1])
  #   for i in range(2,n):
  #     dp[i] = max(dp[i-2]+nums[i], dp[i-1])
  # return dp[n-1]

  # 메모리를 적게 쓰는 방안
  prev, curr = 0,0
  
  for num in nums:
    prev,curr= curr, max(prev+num, curr)
  return curr
   

print(solution([1,2,3,1]))
print(solution([2,7,9,3,1]))