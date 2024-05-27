from bisect import bisect_left

def solution(nums,target):
  answer = bisect_left(nums,target)
  if answer!=len(nums) and nums[answer] == target:
    return answer
  return -1
  # l,r = 0,len(nums)-1

  # while l<=r:
  #   mean = (l+r)//2
  #   if target == nums[mean]:
  #     return mean
  #   elif target>nums[mean]:
  #     l = mean+1
  #   else:
  #     r = mean-1
  # return -1

print(solution(nums = [-1,0,3,5,9,12], target = 9))
print(solution(nums = [-1,0,3,5,9,12], target = 2))