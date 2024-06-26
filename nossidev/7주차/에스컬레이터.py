def solution(n, escalator):
  dp= escalator # dp테이블을 주어진 값(에스컬레이터) 그 자체로 두고 시작
  
  # dp 의 첫번째 줄 채워주기(항상 가운데에서 시작) 
  dp[0][0] = float('inf') if dp[0][0]==1 else 1 # 만약 주어진값(에스컬레이터에서) 1이면 아예 큰 값을 넣어줘서 가지 못하게, 아니라면 1(무조건 가운데에서 시작하니까 한칸 옮기면 1이 count)
  dp[0][1] = float('inf') if dp[0][1]==1 else 0 # 여기서 항상 시작 
  dp[0][2] = float('inf') if dp[0][2]==1 else 1 # 만약 주어진값(에스컬레이터에서) 1이면 아예 큰 값을 넣어줘서 가지 못하게, 아니라면 1(무조건 가운데에서 시작하니까 한칸 옮기면 1이 count)

  # dp 테이블을 2번째 줄 부터 채워나가기 (count의 값을 갱신하면서)
  for floor in range(1,n):
      for loc in range(3): # 열은 항상 3개로 고정
          # 만약 escalator[fllor][loc] == 1이라면 거기로는 가지 못하니까 아예 큰 값을 둬서 min할때 값을 제외할 수 있게하기
          dp[floor][loc] = float('inf') if dp[floor][loc] == 1 else min(dp[floor-1][0]+abs(0-loc), dp[floor-1][1]+abs(loc-1), dp[floor-1][2]+abs(loc-2))
  return min(dp[-1]) # dp테이블의 마지막줄에 모든 값이 갱신되어있을 것임 그 중 가장 작은 값을 고르면 됨 


print(solution(n=8,escalator=[[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 0], [0, 1, 0], [0, 1, 1], [0, 0, 0], [0, 0, 1]]))
print(solution(n=4,escalator=[[0, 1, 0], [1, 0, 1], [1, 0, 1], [0, 0, 1]]))
print(solution(n=5,escalator=[[1, 0, 1], [0, 0, 0], [0, 0, 0], [1, 0, 0], [1, 1, 0]]))