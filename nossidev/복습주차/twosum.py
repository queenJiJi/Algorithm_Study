def solution(nums,target):
  # 완전탐색 (2400ms)
  # for i in range(len(nums)):
  #   for j in range(i+1, len(nums)):
  #     if nums[i]+nums[j] == target:
  #       return [i,j]
      

  # 투포인터 (42ms)
  nums = [[idx,val] for idx,val in enumerate(nums)]
  nums.sort(key = lambda x:x[1])

  l,r = 0, len(nums)-1
  while l<r:
    mean = nums[l][1] + nums[r][1]
    if target > mean:
      l+=1
    elif target<mean:
      r-=1
    else:
      print('l',l,'r',r)
      return [nums[l][0], nums[r][0]]
  return False

  # 백트래킹 (시간초과)
  ans = []
  def backtrack(start):
    if len(ans)==2 and nums[ans[0]]+nums[ans[1]]== target:
      return [ans[0],ans[1]]
    
    for i in range(start,len(nums)):
      ans.append(i)
      result = backtrack(i+1)
      if result:
        return result 
      ans.pop()
  return backtrack(0)


print(solution(nums = [2,7,11,15], target = 9))
print(solution(nums = [3,2,4], target = 6))
print(solution(nums = [3,3], target = 6))
print(solution(nums=[4,9,7,5,1], target= 14))