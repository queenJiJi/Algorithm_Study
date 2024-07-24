from collections import deque, defaultdict

def bfs(graph, start, end ,n ):
  q=deque([start])
  visited=[False]*(n+1)
  visited[start] = True
  visited[end] = True # 끝을 정해주기 위해
  count = 1
  while q:
    start_node = q.popleft()
    for next_node in graph[start_node]:
      if not visited[next_node]:
        q.append(next_node)
        visited[next_node] = True
        count +=1
  return count

def solution(n,wires):
  answer = float('inf')
  graph = defaultdict(list)

  for v1,v2 in wires:
    graph[v1].append(v2)
    graph[v2].append(v1)
 
  for start,end in wires:
    cutted_part = bfs(graph,start,end, n)
    print(cutted_part)
    rest_part = n-cutted_part
    answer = min(answer, abs(cutted_part-rest_part))

  return answer


print(solution(9,[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
print(solution(4,	[[1,2],[2,3],[3,4]]))
print(solution(7	,[[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))