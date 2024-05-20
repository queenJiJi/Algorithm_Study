# dfs 기본 Template (인접리스트)
# graph = {
#     0: [1, 3, 6],
#     1: [0, 3],
#     2: [3],
#     3: [0, 1, 2, 7],
#     4: [5],
#     5: [4, 6, 7],
#     6: [0, 5],
#     7: [3, 5],
# }

# visited=[False] * len(graph)
# def dfs(cur_v):
#   visited[cur_v] = True
#   print(cur_v, end=' ')  

#   for next_v in graph[cur_v]:
#     if not visited[next_v]:
#       dfs(next_v)
# dfs(0)

# dfs Implicit Graph Template
graph = [[1,1,1,1],[0,1,0,1],[0,1,0,1],[1,0,1,1]]
row_len, col_len = len(graph), len(graph[0])
visited = [[False] * col_len for _ in range(row_len) ]

dr = [0,1,0,-1]
dc = [1,0,-1,0]

def dfs(r,c):
  visited[r][c] = True

  for i in range(4): # 4방향일 경우
    next_r = r + dr[i]
    next_c = c + dc[i]
    # print((next_r,next_c), end=' ')

    if 0<=next_r<row_len and 0<=next_c<col_len and graph[r][c] == 1:
      if not visited[next_r][next_c]:
        dfs(next_r,next_c)

dfs(0,0)
