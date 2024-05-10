nums=[1,2,3]
def backtrack(start, cur, result):
  result.append(cur[:])

  for i in range(start,len(nums)):
    cur.append(nums[i])
    backtrack(i+1, cur, result)
    cur.pop()

  return result

print(backtrack(0, [],[]))
