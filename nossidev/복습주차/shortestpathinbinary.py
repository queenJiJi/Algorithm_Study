from collections import deque
def solution(grid):
  n = len(grid)
  q = deque()
  q.append([0,0,1])
  visited=[[False]*n for _ in range(n)]

  if grid[0][0] == 1 or grid[n-1][n-1] == 1:
    return -1

  while q:
    r,c,dist = q.popleft()
    visited[r][c] = True

    if r==n-1 and c==n-1:
      return dist

    for dr,dc in [[-1,0],[1,0],[0,-1],[0,1],[1,1],[1,-1],[-1,1],[-1,-1]]:
      nr,nc = dr+r,dc+c
      if 0<=nr<n and 0<=nc<n and not visited[nr][nc] and grid[nr][nc] == 0:
        q.append([nr,nc,dist+1])
        visited[nr][nc] = True

  return -1





print(solution(grid = [[0,1],[1,0]]))
print(solution(grid = [[0,0,0],[1,1,0],[1,1,0]]))
print(solution(grid = [[1,0,0],[1,1,0],[1,1,0]]))