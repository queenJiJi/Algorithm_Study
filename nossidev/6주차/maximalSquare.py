def solution(matrix):
  # Top-down
  rows = len(matrix)
  cols = len(matrix[0])
  memo = {}

  def dp(r,c):
    if r>=rows or c>= cols: # base case
      return 0
    
    if (r,c) not in memo:
      down = dp(r+1,c)
      right = dp(r,c+1)
      diag = dp(r+1,c+1)

      memo[(r,c)] = 0 # matrix[r][c]=='0'인 경우에도 불필요한 연산을 막기위해 넣어줘야함 
      if matrix[r][c] == '1':
        memo[(r,c)] = min(down,right,diag) +1
    return memo[(r,c)]

  dp(0,0)
  return max(memo.values())**2    
  
  # Bottom-up
  dp = [[0]* (cols+1) for _ in range(rows+1)] # out of bound를 방지하기 위해 일부러 가로,세로 한줄씩 더 크게 시작
  maxlen = 0

  # dp테이블 크기를 한줄씩 크게 만들었기 때문에 (0,0)이 아닌 (1,1)부터 시작해서 dp를 채워나감
  for r in range(1,rows+1):
    for c in range(1,cols+1):
      if matrix[r-1][c-1] =='1': # dp테이블 크기를 한줄씩 크게 만들었기 때문에 matrix에선 각각 -1해줘야 그에 대응하는 위치를 알수있음
        dp[r][c] = min(dp[r-1][c] , dp[r][c-1], dp[r-1][c-1])+1
        maxlen = max(maxlen, dp[r][c]) # 최대길이 나올때마다 업데이트
  return maxlen**2



print(solution([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
print(solution([["0","1"],["1","0"]]))
print(solution([["0"]]))