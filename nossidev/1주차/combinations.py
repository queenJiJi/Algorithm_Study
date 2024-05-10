nums= [1,2,3,4]
k = 2

def backtrack(start, ans, result):
  if len(ans) == k:
    result.append(ans[:])
    return

  for i in range(start, len(nums)):
    ans.append(nums[i])
    backtrack(i+1, ans, result)
    ans.pop()
  return result


print(backtrack(0, [], []))