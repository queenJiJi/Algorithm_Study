def top_down_solution(n):
  # 목표계단수(n) 크기의 memo를 만들고 -1로 초기화한다
  # 현재 계단 순서(n)가 0번째 혹은 1번째 일 경우, 1을 반환(base case)
  # 현재 계단(n)에 도달하는 가짓수가 지정되어있지 않다면, -1일 것
    # n-1번째 ,n-2번째 계단에 대하여 재귀함수 호출(recurrence relation)
  # 현재 계단(n)에 도달하는 총 가짓수를 반환
  memo = [-1] * (n+1)

  def dp(n):
    if n == 0 or n == 1:
      return 1
    
    if memo[n] == -1:
      memo[n] = dp(n-1) + dp(n-2)
    return memo[n]
  return dp(n)


def bottom_up_solution(n):
  # 목표 계단 수(n) 크기의 dp 테이블을 만든다.
  # 0번째,1번째 계단을 1로 지정한다.(base case)
  # 2번째 계단부터 n번째 계단까지 올라간다.
    # 점화식에 따라 각 계단에 도달할 수 있는 총 가짓수를 구한다(recurrence relation)
  # n번째 계단에 도달하는 총 가짓수를 반환한다.

  dp = [-1]* (n+1)

  dp[0] = 1
  dp[1] = 1

  for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]
  
  return dp[n]

print(top_down_solution(2))
print(top_down_solution(3))
print(bottom_up_solution(2))
print(bottom_up_solution(3))