# Top Down
# def solution(cost):
#   memo = {} # list로 해도 상관없음

#   def dp(n):
#     if n==0 or n==1:
#       return 0
#     if n not in memo:
#       memo[n] = min(dp(n-1)+cost[n-1], dp(n-2)+cost[n-2])
#     return memo[n]
#   return dp(len(cost))


# Bottom Up
def solution(cost):
  n = len(cost)
  dp=[-1]*(n+1) #dict로 해도 상관없음

  dp[0]=0
  dp[1]=0

  for i in range(2,n+1):
    dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
  return dp[n]


print(solution([10,15,20]))
print(solution([1,100,1,1,1,100,1,1,100,1]))