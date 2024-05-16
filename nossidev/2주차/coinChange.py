# SOL1 - DP
# def solution(coins, amount):

#   dp = [amount+1] * (amount+1)

#   dp[0] = 0

#   for x in range(1,amount+1):
#     for coin in coins:
#       if x-coin >=0:
#         dp[x] = min(dp[x],1+dp[x-coin])
#   return dp[amount] if dp[amount] != amount +1 else -1 # defaultvalue가 아닐때 return

# SOL2 - BFS
from collections import deque
def solution(coins, amount):
    # 초기 금액을 amount, 동전 개수를 0으로 설정하고, 큐에 추가한다.
    q = deque()
    q.append((amount,0))
    visited = set()
    # 큐가 빌 때까지 반복문을 수행한다.
    while q:
        # 큐에서 현재 남은 금액과 현재 동전 개수를 popleft한다.
        cur_amount, num_coins = q.popleft()       
        # 현재 남은 금액이 0이라면 현재 동전 개수를 반환한다.
        if cur_amount ==0:
            return num_coins
        # 한 동전을 사용해서 다음 남은 금액을 만든다.
        for coin in coins:
            next_coin = cur_amount-coin       
            # 다음 남은 금액이 처음 발생하고, 액수가 0 이상이라면,
            if next_coin not in visited and next_coin >=0:          
              # 다음 남은 금액과 동전 개수에 1을 더해서 큐에 추가한다.
              q.append((next_coin, num_coins+1))
              # visited에 다음 남은 금액을 추가한다.
              visited.add(next_coin)
    # coins의 동전으로 amount를 만들 수 없다면 -1을 반환한다.
    return -1

print(solution([1,2,5], 11))
print(solution([2], 3))
print(solution([1], 0))