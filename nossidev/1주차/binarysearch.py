from bisect import bisect_left
nums = [-1,0,3,5,9,12]
target = 9

def sol():
  nums.sort()
  ans = bisect_left(nums,target)
  if ans!=len(nums) and nums[ans] == target:
      return ans
  return -1

print(sol())
