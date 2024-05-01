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

start_v = 0
visited = [False] * len(graph)

def dfs(graph, cur_v, visited):
  visited[cur_v] = True  # 현재 노드를 방문했다고 표시
  print(cur_v, end = ' ') # 방문한 노드 출력

  for next_v in graph[cur_v]:
    if not visited[next_v]:
      dfs(graph, next_v, visited)
  

dfs(graph,start_v,visited)