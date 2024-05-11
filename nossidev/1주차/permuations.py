# SOL1 - itertools

# from itertools import permutations,combinations

# nums = [1,2,3]
nums= [[4,3],[2,2],[2,2]]
# nums = [0,1]
# nums = [1]

# n = len(nums)
# print(list(permutations(nums, n)))


# SOL2 - backtracking

def backtracking(cur):
  n = len(nums)
  ans = []
  # base case
  if len(cur) == n:
    print(cur)
    ans.append(cur[:]) 
    return
  
  for num in nums:
    if num not in cur:
      cur.append(num)
      backtracking(cur)
      cur.pop()

print(backtracking(cur=[]))
