from collections import deque

# [SOL1]
# def solution(graph):
#   # visited : 노드의 방문 여부와 해당 노드가 어떤 세트에 속하는지를 나타내기 위해 사용
#   visited = [0] * len(graph) # setA: -1, setB: 1
  
#   def bfs(start_v):
#     if visited[i]: # 이미 값이 들어갔다는 의미 = 이미 방문을 한번 했음 
#       return True # 이미 방문한 노드에 대해서는 추가 작업을 하지 않을 것 
    
#     q= deque() 
#     q.append(start_v)
#     visited[start_v] = -1 # setA 
#     while q:
#       cur_v = q.popleft()

#       for next_v in graph[cur_v]:
#         if visited[next_v] == visited[cur_v]: # 인접한 노드끼리 같은 세트내에 포함되었다면
#           return False
#         elif not visited[next_v]: # 방문안한 노드라면
#           q.append(next_v)
#           visited[next_v] = -1 * visited[cur_v] # setB
#     return True


#   for i in range(len(graph)):
#     if not bfs(i): # bfs를 다 돌았는데 돌지 않은 노드가 있다면 
#       return False 
#   return True

# [SOL 2] - bfs
# def solution(graph):
#   visited = [0] * len(graph)
#    # 모든 노드에 대해 반복
#   for i, color in enumerate(visited):
#     if color==0:
#       q = deque([i])
#       visited[i] = 1

#       while q:
#         cur_v = q.popleft()

#         for next_v in graph[cur_v]:
#           if visited[next_v] == 0:
#             visited[next_v] = visited[cur_v]*-1
#             q.append(next_v)
#           elif visited[next_v] == visited[cur_v]:
#             return False
#   return True

# [SOL 3] - dfs
def solution(graph):
  visited = [0] * len(graph)
   
  def dfs(cur_v):
    for next_v in graph[cur_v]:
      if visited[next_v] == 0:
        visited[next_v] = -1*visited[cur_v]
        if not dfs(next_v):
          return False
      elif visited[next_v] == visited[cur_v]:
        return False
    return True


  for i in range(len(graph)): # 모든 노드에 대해 반복
    if visited[i] == 0: # 만약 방문하지 않았다면 탐색 시작
      visited[i] = 1 # 첫 노드를 1로 표시. DFS시작
      if not dfs(i):
        return False 
  return True 
   

print(solution([[1,2,3],[0,2],[0,1,3],[0,2]]))
print(solution([[1,3],[0,2],[1,3],[0,2]]))