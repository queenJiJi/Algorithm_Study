# 최단 거리/최단 경로 찾기(ex.미로찾기) 문제는 BFS로 풀기!!!!
  # 너비 우선 탐색이니까 BFS가 훨씬 나은 접근임!

from collections import deque
def shortestPath(grid):
  path_count = -1
  row,col = len(grid), len(grid[0])
  visited = [[False]*col for _ in range(row)]
  q = deque()
  q.append((0,0,1))
  visited[0][0] = True
  # 애초에 갈 수 경로가 없는 경우: grid에 하나만 있는 경우, 첫 시작이 1인 경우 return -1
  if grid[0][0]== 1 or grid[0][0]== []:
    return -1
  
  while q:
    cur_x, cur_y,path = q.popleft()
    if cur_x == (row-1) and cur_y == (col-1): # 목적지에 도착했을 때
      path_count = path
      break
    visited[cur_x][cur_y] = True 
    # 대각선도 다 연결되어있으니까 방향이 8가지임
    dr = [-1, 1, 0, 0, -1, -1,1,1]
    dc = [0, 0, -1, 1, 1, -1,1,-1]    
    for i in range(8):
      next_x = cur_x + dr[i]
      next_y = cur_y + dc[i]

      if next_x>=0 and next_x<row and next_y>=0 and next_y<col:
        if visited[next_x][next_y]==False and grid[next_x][next_y] ==0:
          q.append((next_x, next_y,path+1))
          visited[next_x][next_y] = True
  return path_count


print(shortestPath(grid = [[0,0,0],[1,1,0],[1,1,0]]))
print(shortestPath(grid = [[1,0,0],[1,1,0],[1,1,0]]))