from itertools import permutations

def backtrack(k,dungeons,cnt,visited):
    n = len(dungeons)
    answer = cnt # 현재까지의 카운트 값으로 초기화

    for i in range(n):
       if k>=dungeons[i][0] and not visited[i]:
          visited[i] = True # 던전 방문처리
          answer = max(answer, backtrack(k-dungeons[i][1], dungeons, cnt+1,visited))
          visited[i] = False # 백트래킹을 위해 방문해제
    return answer    
    
def solution(k,dungeons):
    # n = len(dungeons)
    # all = list(permutations(dungeons,n))
    # answer = 0
    # for a in all:
    #   cnt =0
    #   newk = k
    #   for i in range(len(a)):
    #     if newk >= a[i][0]:
    #       newk -= a[i][1] 
    #       cnt+=1
    #     else:
    #       break
    #   answer=max(answer,cnt)
    # return answer
    visited = [False] * len(dungeons) 
    return backtrack(k,dungeons,0, visited)
print(solution(80,[[80,20],[50,40],[30,10]]))