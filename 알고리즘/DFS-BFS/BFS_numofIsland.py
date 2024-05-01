from collections import deque

grid=[
  [1,1,0,0,0],
  [1,1,0,0,0],
  [0,0,1,0,0],
  [0,0,0,1,1]
]

def numOfIsland(board):
  row = len(grid)
  col = len(grid[0])
  visited = [[False]*col for _ in range(row)]
  num_of_island = 0

  def bfs(board,r,c):
    q= deque()
    q.append((r,c))
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    visited[r][c] = True
    while q:
      cur_r, cur_c = q.popleft()
      for i in range(4):
        next_r = cur_r +dr[i]
        next_c = cur_c +dc[i]

        if next_r>=0 and next_r<row and next_c>=0 and next_c<col: # board 가 out of range가 아니면서
          if visited[next_r][next_c]== False and board[next_r][next_c] == 1: # 처음 방문하고(visited:False) & 섬일 경우(board == 1)
            q.append((next_r, next_c))
            visited[next_r][next_c] = True

  for r in range(row):
    for c in range(col):
      if board[r][c] == 1 and visited[r][c] == False:
        bfs(board,r,c)
        num_of_island+=1
  return num_of_island


print(numOfIsland(grid))