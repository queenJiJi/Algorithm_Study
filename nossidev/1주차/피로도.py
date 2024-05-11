from itertools import permutations
# def solution(k, dungeons):
#   def calculation(arr,k):
#     count =0
#     for i in range(len(arr)):
#       print(arr[i][0], arr[i][1])
#       if k >=arr[i][0]:
#         k = k-arr[i][1]
#         count+=1
#       else: continue
#     return count
  
#   def backtracking(cur):
#     n = len(dungeons)
#     # base case
#     if len(cur) == n:
#       print(cur)
#       # case.append(calculation(cur,k)) 
#       return 
    
#     for num in dungeons:
#       if num not in cur:
#         cur.append(num)
#         backtracking(cur)
#         cur.pop()
#   case = []
#   backtracking([])
#   return max(case)

# [SOL1] itertools 사용
# def solution(k,dungeons):
#   cases = list(permutations(dungeons,len(dungeons)))
#   count =0
#   result = 0
#   remain = k
#   for i in range(len(cases)):
#     for j in cases[i]:
#       if remain >= j[0]:
#         remain= remain -j[1]
#         count+=1
#       result = max(count,result)
#       # else:
#       #   continue
#       # result.append(count)
#     count =0
#     remain = k
#   return result

# [SOL2] 백트래킹(permutation)으로 완전탐색 
def solution(k,dungeons):
  n = len(dungeons)
  answer = 0
  visited =[0] *n
  def backtrack(k,count):
    nonlocal answer
    # count 값 업데이트
    if count >= answer:
      answer = count

    # dungeons를 순회한다
    for i in range(n):
      # 현재 피로도 k가 i번째 던전의 필요피로도보다 크거나 같으면서, 방문한적이 없으면
      if k>=dungeons[i][0] and not visited[i]:
        # i번째 원소를 방문
        visited[i] = True
        # 재귀함수 호출
        backtrack(k-dungeons[i][1], count+1)
        # i번째 원소 방문을 취소
        visited[i] = False
  backtrack(k,0)
  return answer


print(solution(k=80,dungeons=[[80,20],[50,40],[30,10]]))
print(solution(k=4,dungeons=[[4,3],[2,2],[2,2]]))