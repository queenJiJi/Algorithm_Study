# bfs
# from collections import deque
# def solution(rooms):
#   visited= [False]*len(rooms)
#   q= deque()
#   def bfs(start_v):
#     q.append(start_v)
#     visited[start_v] = True

#     while q:
#       cur_v = q.popleft()
#       for next_v in rooms[cur_v]:
#         if not visited[next_v]:
#           q.append(next_v)
#           visited[next_v] = True
#     return True if all(visited) else False
#   return bfs(0)

# dfs
def solution(rooms):
  visited=[False]*len(rooms)
  
  def dfs(cur_v):
    visited[cur_v] = True
    for next_v in rooms[cur_v]:
      if not visited[next_v]:
        dfs(next_v)
    return True if all(visited) else False
  return dfs(0)




print(solution([[1],[2],[3],[]]))
print(solution([[1,3],[3,0,1],[2],[0]]))