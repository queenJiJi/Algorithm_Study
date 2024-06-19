from collections import deque

def solution(coins, amount):
  # SOL1 - BFS
  # q = deque()
  # visited=set()
  # q.append((amount,0))

  # while q:
  #   cur_amount, coin_num = q.popleft()
  #   visited.add(cur_amount)

  #   if cur_amount ==0:
  #     return coin_num
    
  #   for coin in coins:
  #     next_amount = cur_amount - coin
  #     if next_amount>=0 and next_amount not in visited:
  #       visited.add(next_amount)
  #       q.append((next_amount, coin_num+1))

  # return -1 


  # SOL 2 - Bottom-up
  dp = [float('inf')]* (amount +1)
  
  dp[0] = 0 # base case

  for a in range(1,amount+1): # 1부터 amount까지 
    for c in coins: # 각 coin을 하나씩 돌아보며
      if a-c >= 0: # 만약 amount-coin이 음수라면 남은 금액이 음수니 더이상 진행 불가
        dp[a] = min(dp[a], dp[a-c] + 1) # dp[a-c]는 c에서 coin을 한개 쓴것이니 +1
  return -1 if dp[amount] == float('inf') else dp[amount]
  


print(solution([1,2,5], 11))
print(solution([2], 3))
print(solution([1], 0))