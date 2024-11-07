def solution(num, arr):
  result = []
  arr = sorted(arr)
  def backtrack(tmp,start):

    if len(tmp) == num:
      result.append(tmp[:])
      return
    
    for i in range(start,len(arr)):
        tmp.append(arr[i])
        backtrack(tmp,i+1)
        tmp.pop()

  backtrack([],0)
  result.sort()
  return result 


print(solution(1,[4,5,2]))
print(solution(2,[9,8,7,1]))
print(solution(4,[1231, 1232, 1233, 1234]))
