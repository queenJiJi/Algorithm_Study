from collections import deque,defaultdict
def solution(n, prerequisites):
  graph = defaultdict(list)
  indegree= [0] * n
  visited = [False] * n
  for u,v in prerequisites:
    graph[v].append(u)
    indegree[u] += 1
  q=deque()
  for i in range(n):
    if indegree[i] == 0:
      q.append(i)
  
  while q:
    cur_node = q.popleft()
    visited[cur_node] = True

    for next_node in graph[cur_node]:
        indegree[next_node] -= 1
        if indegree[next_node] == 0:
          q.append(next_node)

  return True if all(visited) else False
print(solution(2,[[1,0]]))
print(solution(2,[[1,0],[0,1]]))