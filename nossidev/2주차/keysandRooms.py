from collections import defaultdict, deque
def solution(rooms):
  
  graph = defaultdict(list)
  for idx,val in enumerate(rooms):
    graph[idx]= val 
  # print(graph)
  
  # BFS SOL
  start_v = 0
  visit= [False]* len(rooms)

  def bfs(start_v):
    q = deque()
    q.append(start_v)
    while q:
      print(q)
      cur_v = q.popleft()
      visit[cur_v] = True
      
      for next_v in graph[cur_v]:
        # if next_v not in visit: # visit이 hashtable형태일때 
        if not visit[next_v]: # visit이 list형태일때
          q.append(next_v)
          visit[next_v] = True
  bfs(0)
  return all(visit)


  # DFS SOL
  def dfs(cur_v):
    visit[cur_v] = True
    
    for next_v in graph[cur_v]:
      if not visit[next_v]:
        dfs(next_v)
  dfs(0)
  return all(visit)

print(solution(rooms = [[1],[2],[3],[]])) 
print(solution(rooms = [[1,3],[3,0,1],[2],[0]]))