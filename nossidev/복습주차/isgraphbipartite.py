# bfs
# from collections import deque
# def solution(graph):
#   n = len(graph)
#   visited= [0] * n

#   q=deque()

#   def bfs(start_v):
#     q.append(start_v)
#     visited[start_v] = 1

#     while q:
#       cur_v = q.popleft()

#       for next_v in graph[cur_v]:
#         if visited[next_v]== visited[cur_v]:
#           return False
#         elif visited[next_v] == 0:
#           visited[next_v] = -1*visited[cur_v]
#           q.append(next_v)
#     return True

#   for i in range(n):
#     if visited[i]==0:
#       visited[i] = 1
#       if not bfs(i):
#         return False
#   return True

# dfs
def solution(graph):
  n = len(graph)
  visited=[0]*n

  def dfs(cur_v):
    for next_v in graph[cur_v]:
      if visited[next_v] == visited[cur_v]:
        return False
      elif visited[next_v] == 0:
        visited[next_v] = visited[cur_v] * -1
        if not dfs(next_v):
          return False
    return True
  
  for i in range(n):
    if visited[i]==0:
      visited[i] = 1
      if not dfs(i):
        return False
  return True
  
print(solution([[1,2,3],[0,2],[0,1,3],[0,2]]))
print(solution([[1,3],[0,2],[1,3],[0,2]]))