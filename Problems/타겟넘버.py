answer= 0
def DFS(numbers,target,idx,cur_val):
  global answer
  N = len(numbers)
  if N == idx and cur_val == target:
    answer+=1
    return
  if N == idx:
    return
  
  DFS(numbers,target,idx+1, cur_val+numbers[idx])
  DFS(numbers,target,idx+1, cur_val-numbers[idx])


def solution(numbers,target):
  global answer

  DFS(numbers,target,0,0)

  return answer



print(solution([1,1,1,1,1],3))
print(solution([4,1,2,1],4))

