def solution(m,n):
  dp = [[1]*(n+1) for _ in range(m+1)]
  
  for r in range(2,m+1):
    for c in range(2,n+1):
      dp[r][c] = dp[r][c-1] + dp[r-1][c]
      
  return dp[m][n]

print(solution(3,7))