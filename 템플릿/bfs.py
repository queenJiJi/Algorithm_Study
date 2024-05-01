from collections import deque
graph = {
    0: [1, 3, 6],
    1: [0, 3],
    2: [3],
    3: [0, 1, 2, 7],
    4: [5],
    5: [4, 6, 7],
    6: [0, 5],
    7: [3, 5],
}

start_v= 0

def bfs(graph, start_v):
  visited = {start_v:True}
  q= deque()
  q.append(start_v)

  while q:
    cur_v = q.popleft()

    for next_v in graph[cur_v]:
      if next_v not in visited: # 아직 방문을 하지 않았다면
        q.append(next_v)
        visited[next_v] = True
  return [i for i in visited.keys()]


print(bfs(graph,start_v))