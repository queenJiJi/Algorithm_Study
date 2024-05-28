from collections import deque
def solution(grid):
  count = 0
  row_len,col_len = len(grid), len(grid[0])
  visited = [[False]*col_len for _ in range(row_len)]
  q= deque()

  # def bfs(r,c):
  def dfs(r,c):
    # q.append((r,c))
    visited[r][c] = True

    for dr,dc in [[-1,0],[1,0],[0,-1],[0,1]]:
      nr,nc = r+dr, c+dc
      if 0<=nr<row_len and 0<=nc<col_len and grid[nr][nc]=='1' and not visited[nr][nc]:
        dfs(nr,nc)

    # while q:
    #   cur_r,cur_c = q.popleft()
      
    #   for dr,dc in [[-1,0],[1,0],[0,-1],[0,1]]:
    #     nr,nc = cur_r+dr, cur_c+dc
    #     if 0<=nr<row_len and 0<=nc<col_len and grid[nr][nc]=='1' and not visited[nr][nc]:
    #       q.append((nr,nc))
    #       visited[nr][nc] =True

  for r in range(row_len):
    for c in range(col_len):
      if grid[r][c] == '1' and not visited[r][c]:
          # bfs(r,c)
          dfs(r,c)
          count+=1
  return count
print(solution(grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))
print(solution(grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))