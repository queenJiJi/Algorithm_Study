def cs(n):
  # Top Down 방식(재귀) : 1. 재귀 탈출 조건 필요 2. 재귀 점화식 사용
   # dp를 통해 memoization해주는 것은 bottom up과 동
  # memo = [-1] * (n+1)
  # def dp(n):
  #   if n == 0 or n== 1:
  #     return 1 
  #   if memo[n] == -1:
  #     memo[n] = dp(n-1) + dp(n-2)
  #   return memo[n]
  # return dp(n)

  # Bottom Up 방식(반복문) : 1. for 반복문 사용 2. dp테이블을 반복적으로 사용
    #                                         -> dp테이블을 하나씩 채워나가는 개념 
    # dp를 통해 memoization해주는 것은 top down과 동일 
    # 연산 속도가 top down보다 빠름!
  dp = [-1]* (n+1)

  dp[0] = 1
  dp[1] = 1

  for i in range(2,n+1):
    dp[i] = dp[i-1] + dp[i-2]
  return dp[n]

print(cs(2))
print(cs(3))
print(cs(44))
