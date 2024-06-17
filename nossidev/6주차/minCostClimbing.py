def solution(cost):
  n = len(cost)
  # # top-down
  # # memo=[-1]* (n+1) # 리스트 형식
  # memo = {} # 딕셔너리 형식

  # def dp(n):
  #   if n==0 or n==1:
  #     return 0
    
  #   # if memo[n] == -1: # 리스트형식
  #   if n not in memo: # 딕셔너리 형식
  #     memo[n] = min(dp(n-1)+cost[n-1], dp(n-2)+cost[n-2])
  #   return memo[n]
  # return dp(n)

  # bottom-up
  dp = [-1] * (n+1)
  
  dp[0] = 0
  dp[1] = 0
  
  for i in range(2,n+1):
    dp[i] = min(dp[i-1]+cost[i-1] , dp[i-2]+cost[i-2])
    print(dp)
  return dp[n]



print(solution(cost = [10,15,20]))
print(solution(cost = [1,100,1,1,1,100,1,1,100,1]))