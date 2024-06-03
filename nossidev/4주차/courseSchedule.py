from collections import deque
def solution(n, prerequisites):
  visited = []
  indegree = [0] * n
  graph = [[] for _ in range(n)]

  for v,u in prerequisites:
    graph[u].append(v)
    indegree[v] +=1

  q = deque()
  for node in range(n):
    if indegree[node]==0:
      q.append(node)
  
  while q:
    cur_v = q.popleft()
    visited.append(cur_v)

    for next_v in graph[cur_v]:
      indegree[next_v] -= 1

      if indegree[next_v] == 0:
        q.append(next_v)
  return True if len(visited) == n else False

print(solution(2,[[1,0]]))
print(solution(2,[[1,0],[0,1]]))