from collections import deque
# bfs 기본 Template (인접리스트)
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

# visited= [False] * len(graph)
# def bfs(start_v):
#   q=deque()
#   q.append(start_v)

#   while q:
#     cur_v = q.popleft()
#     visited[cur_v] = True
#     print(cur_v, end = ' ')

#     for next_v in graph[cur_v]:
#       if not visited[next_v]:
#         q.append(next_v)
#         visited[next_v] = True
# bfs(0)

# bfs Implicit Graph Template
graph = [[1,1,1,1],[0,1,0,1],[0,1,0,1],[1,0,1,1]]

def bfs(r,c):
  row_len,col_len = len(graph), len(graph[0])
  visited= [[False]*col_len for _ in range(row_len)]

  #8가지 방향일때 
    # 상 하 좌 우 왼아래 오아래 왼위 오른위
  dr = [-1, 1, 0, 0, 1, 1, 0, -1, -1] 
  dc = [0, 0, -1, 1, -1, 1, -1, 1]
  
  q = deque()
  q.append((r,c))
  visited[r][c] = True

  while q:
     cur_r, cur_c = q.popleft()
    #  print((cur_r,cur_c), end=' ')
     for i in range(8): # 8가지 방향일 경우
        next_r = cur_r+dr[i]
        next_c = cur_c+dc[i]

        if 0<=next_r<row_len and 0<=next_c<col_len and graph[next_r][next_c]==1:
           if not visited[next_r][next_c]:
            q.append((next_r,next_c))
            visited[next_r][next_c] = True
bfs(0,0)


