# bfs 는 무조건 Q !!!!!
from collections import deque

graph = {
  'A':['B','D','E'],
  'B':['A','C','D'],
  'C':['B'],
  'D':['A','B'],
  'E':['A']
}


def bfs(graph, start_v):
  visited=[start_v]
  q=deque(start_v)
  
  while q:
    cur_v = q.popleft()
    for i in graph[cur_v]:
      if i not in visited:
        q.append(i)
        visited.append(i)
  return visited

print(bfs(graph,'A'))