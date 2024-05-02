# top down
# def solution(m,n):
#   memo = [[-1]*n for _ in range(m)]

#   def dp(r,c):
#     if r==0 and c== 0:
#       memo[r][c] = 1
#       return memo[r][c] 

#     if memo[r][c] == -1: 
#       path_count = 0
#       if (r-1) >=0:
#         path_count += dp(r-1,c)
#       if (c-1) >=0:
#         path_count += dp(r,c-1)
#       memo[r][c] = path_count
#     return  memo[r][c]
    
#   return dp(m-1,n-1)


# bottom up
def solution(m,n):
  dp = [[-1]*n for _ in range(m)]

  for r in range(m):
    dp[r][0] = 1
  for c in range(n):
    dp[0][c] = 1

  for r in range(1,m):
    for c in range(1,n):
      dp[r][c] = dp[r-1][c] + dp[r][c-1]

  return dp[m-1][n-1] 


print(solution(3,7))
print(solution(3,2))
  