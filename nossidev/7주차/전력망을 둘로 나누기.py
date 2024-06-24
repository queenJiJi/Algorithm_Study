from collections import deque, defaultdict
def bfs(graph,start,end,n):
  q = deque([start])
  visited = [False]*(n+1)
  visited[start] = True
  visited[end] = True # start,end사이의 간선이 잘린거니까 end는 방문하면 안되니까 아싸리 방문처리를 해주면 여긴 돌지 못할것
  count = 1

  while q:
    cur_v = q.popleft()

    for next_v in graph[cur_v]:
      # if not visited[next_v] and next_v!=end: # 이렇게해서 end를 방문 못하게 하는 방법도 있음(visited[end]=True를 안했을 시)
      if not visited[next_v]:
        q.append(next_v)
        visited[next_v] = True
        count+=1
  return count

def solution(n,wires):
  graph=defaultdict(list)
  answer = float('inf')

  for x,y in wires:
    graph[x].append(y)
    graph[y].append(x)

  
  for start,endpoint in wires:
    result1 = bfs(graph,start,endpoint,n)
    # 원래 나머지(잘린노드부터 다시 시작하는 나눠진 트리중 나머지 트리도 순회해야하는데, n에서 result1의 갯수를 빼주면 그게 어짜피 result2일 것임
    # result2 = bfs(graph,cases[1],cases[0], n) 
   
    answer = min(answer, abs(n-result1-result1)) # result2의 갯수가 n-result1일 것이고, result2와 result1의 차이가 가장 작아야하니까 abs(result1-result2)

  return answer


print(solution(9,[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
print(solution(4,[[1,2],[2,3],[3,4]]))
print(solution(7,[[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))