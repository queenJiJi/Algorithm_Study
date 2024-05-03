nums= [1,2,3,4]

# 순열
def permute(nums):
  ans= []
  def backtracking(curr):
    # 탈출조건
    if len(curr) == len(nums):
        ans.append(curr[:])
        return
    
    for num in nums:
       if num not in curr:
          curr.append(num)
          backtracking(curr)
          curr.pop()
  backtracking(curr=[])
  return ans

print(permute(nums))
print()

# 조합
def comb(nums,k):
  result=[]
  def backtracking(start,curr):
    if len(curr) == k:
        result.append(curr[:])
        return
    
    for i in range(start, len(nums)):
        curr.append(nums[i])
        backtracking(i+1,curr)
        curr.pop()
  backtracking(start=0, curr=[])
  return result

print(comb(nums,k=2))
print()


# 부분집합
def sol(nums):
  result=[]
  def backtracking(start,curr):
    if len(curr) == k:
        result.append(curr[:])
        return
    
    for i in range(start, len(nums)):
        curr.append(nums[i])
        backtracking(i+1,curr)
        curr.pop()
  for k in range(len(nums)+1):
    backtracking(start=0, curr=[])
  return result

print(sol(nums))
print()
