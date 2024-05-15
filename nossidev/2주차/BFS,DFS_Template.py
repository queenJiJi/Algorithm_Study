from collections import defaultdict, deque
n = 6
edge_set = [[1, 2], [2, 6], [2, 4], [4, 3], [3, 2], [3, 5]]
edge_set = [[0,1],[0,3],[0,6],[1,0],[1,3],[2,3],[3,0],[3,1],[3,2],[3,7],
            [4,5],[5,4],[5,6],[5,7],[6,0],[6,5],[7,3],[7,5]]

graph = defaultdict(list)

for u,v in edge_set:
  graph[u].append(v)

# print(graph)

start_v = 0
def bfs(start_v):
  visited={start_v:True}
  q = deque()
  q.append(start_v)

  while q:
    cur_v = q.popleft()
    visited[cur_v] = True

    for next_v in graph[cur_v]:
      if next_v not in visited:
        q.append(next_v)
        visited[next_v] = True

  return [i for i in visited.keys()]

print(bfs(0))


visited = {}
def dfs(cur_v):
  visited[cur_v] = True
  print(cur_v, end=' ')
  
  for next_v in graph[cur_v]:
    if next_v not in visited:
      dfs(next_v)

dfs(0)