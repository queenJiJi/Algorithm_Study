grid=[
  [1,1,0,0,0],
  [1,1,0,0,0],
  [0,0,1,0,0],
  [0,0,0,1,1]
]

def numOfIsland(board): 
  num_of_island = 0
  row_len = len(grid)
  col_len = len(grid[0])
  visited = [[False]* col_len for _ in range(row_len)]

  def dfs(r,c):
    dr= [-1,1,0,0]
    dc= [0,0,-1,1]
    visited[r][c] = True

    for i in range(4):
      nr = r+dr[i]
      nc = c+dc[i]
      if nr>=0 and nr<row_len and nc>=0 and nc<col_len:
        if board[nr][nc]==1 and visited[nr][nc]==False:
          dfs(nr,nc)

  for row in range(row_len):
    for col in range(col_len):
      if board[row][col] == 1 and visited[row][col] == False:
        dfs(row,col)
        num_of_island+=1

  return num_of_island

print(numOfIsland(grid))