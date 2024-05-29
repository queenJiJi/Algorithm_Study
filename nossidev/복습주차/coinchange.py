from collections import deque

def solution(coins, amount):
  q = deque()
  q.append((amount,0))
  visited=set()
  while q:
    cur_amount,num_coins = q.popleft()
    visited.add(cur_amount)
    if cur_amount == 0:
      return num_coins

    for coin in coins:
      next_amount = cur_amount-coin
      if next_amount >= 0 and next_amount not in visited:
        visited.add(next_amount)
        q.append((next_amount,num_coins+1)) 
  return -1


print(solution([1,2,5], 11))
print(solution([2], 3))
print(solution([1], 0))