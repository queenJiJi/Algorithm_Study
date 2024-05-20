from collections import deque
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

row_len,col_len= len(grid), len(grid[0])
visited=[[False]*col_len for _ in range(row_len)]
dr = [-1,1,0,0]
dc = [0,0,-1,1]
count = 0

def dfs(r,c):
  visited[r][c] = True

  for i in range(4):
    next_r= r+dr[i]  
    next_c= c+dc[i]  

    if 0<=next_r<row_len and 0<=next_c<col_len and grid[next_r][next_c] == "1":
      if not visited[next_r][next_c]:
        dfs(next_r, next_c)


# def bfs(r,c):
#   q = deque()
#   q.append((r,c))
  
#   while q:
#     cur_r,cur_c = q.popleft()
#     visited[cur_r][cur_c] = True

#     for i in range(4):
#       next_r= cur_r+dr[i]  
#       next_c= cur_c+dc[i]  

      # if 0<=next_r<row_len and 0<=next_c<col_len and grid[next_r][next_c] == "1":
      #   if not visited[next_r][next_c]:
      #     q.append((next_r,next_c))
      #     visited[next_r][next_c] = True

for i in range(row_len):
  for j in range(col_len):
    if grid[i][j] == "1" and not visited[i][j]:
      # bfs(i,j)
      dfs(i,j)
      count+=1
print(count)