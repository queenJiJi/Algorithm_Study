from collections import deque


def solution(maps):
  n = len(maps)
  m= len(maps[0])
  visited = [[False]*m for _ in range(n)]
  
  q= deque()
  q.append([0,0])
  visited[0][0] = True
  dist = 1

  while q:
    cur_r,cur_c = q.popleft()
  
    if (cur_r,cur_c) ==(n-1,m-1):
      return maps[cur_r][cur_c]

    for dr,dc in [[0,1],[0,-1],[-1,0],[1,0]]:
      nr,nc= cur_r+dr, cur_c+dc 
      if 0<=nr<n and 0<=nc<m and not visited[nr][nc] and maps[nr][nc]==1:
        visited[nr][nc]= True
        q.append([nr,nc])
        dist+=1
        maps[nr][nc] = maps[cur_r][cur_c]+1
        print((nr,nc))
        for i in maps:
          print(*i)
        print()
        print('dist',dist)
  return -1 

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
# print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))