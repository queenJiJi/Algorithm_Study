# all(리스트) : 리스트안의 모든 값이 True일때 true 반환, 하나라도 False라면 False 반환

# SOL1 - DFS
# def keysAndRooms(rooms):
#   visited= [False]*len(rooms)

#   def dfs(start_v):
#     visited[start_v] = True

#     for next_v in rooms[start_v]:
#       if visited[next_v] == False:
#         dfs(next_v)
#     return visited 
  
#   dfs(0)

#   return True if all(visited) else False 


# SOL2 - BFS
from collections import deque

def keysAndRooms(rooms):
  visited= [False]*len(rooms)
  q = deque()

  def bfs(start_v):
    q.append(start_v)
    visited[start_v] = True
    while q:
      cur_v = q.popleft() 
      for next_v in rooms[cur_v]:
        if visited[next_v] == False:
          q.append(next_v)
          visited[next_v] = True
    return visited

  bfs(0)

  return True if all(visited) else False


print(keysAndRooms(rooms=[[1],[2],[3],[]]))
print(keysAndRooms(rooms=[[1,3],[3,0,1],[2],[0]]))
print(keysAndRooms(rooms=[[],[1],[2]]))


