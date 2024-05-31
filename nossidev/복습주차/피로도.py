# 완전탐색으로 갈 수 있는 모든 경우의 수 (순열)를 나열 -> 그 경우의 수들을 하나씩 해보면 그중 max return

# [SOL1] itertools 사용
from itertools import permutations
def solution(k,dungeons):
  remain = k
  case = list(permutations(dungeons,len(dungeons)))
  result=0
  for i in range(len(case)):
    count =0
    for j in case[i]:
      if remain >= j[0]:
        remain-=j[1]
        count+=1
    remain = k
    result = max(result, count)

  return result


# [SOL2] backtrack사용
# def solution(k,dungeons):
#   answer= 0
#   n = len(dungeons)
#   visited = [0] * n

#   def backtrack(k,count):
#     nonlocal answer
#     # base case
#     if count > answer:
#       answer = count

#     for i in range(n):
#       if k>=dungeons[i][0] and not visited[i]:
#         visited[i] = True
#         backtrack(k-dungeons[i][1], count+1)
#         visited[i] = False    
#     return answer
#   return backtrack(k,0) 
print(solution(80,[[80,20],[50,40],[30,10]]))