def solution(nums,target):
  nums = [[idx,val] for idx,val in enumerate(nums)]
  nums.sort(key=lambda x:x[1])
  l, r = 0, len(nums)-1
  while l<r:
    twosum = nums[l][1] + nums[r][1]

    if target>twosum:
      l+=1
    elif target<twosum:
      r-=1
    else:
      return [nums[l][0], nums[r][0]]
  return False
print(solution(nums=[2,7,11,15],target=9))
print(solution(nums=[3,2,4],target=6))


