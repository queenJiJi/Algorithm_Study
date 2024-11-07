def solution(num, arr):
  result = []

  def backtrack(tmp):

    if len(tmp) == num:
      result.append(tmp[:])
      return
    for val in arr:
      if val not in tmp:
        tmp.append(val)
        backtrack(tmp)
        tmp.pop()
  backtrack([])
  result.sort()
  return result 


print(solution(1,[4,5,2]))
print(solution(2,[9,8,7,1]))