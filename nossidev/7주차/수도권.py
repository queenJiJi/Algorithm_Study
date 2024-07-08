import collections, heapq

def solution(n,k,capitals,edges):

  graph = collections.defaultdict(list)

  for u,v,w in edges:
    graph[u].append((w,v))  
    graph[v].append((w,u))  

  capital_set = set(capitals)
  pq = []
  costs = [float('inf')]*(n+1)

  for capital in capitals:
    heapq.heappush(pq,(0,capital))
    costs[capital] = 0

  while pq:
    cur_cost, cur_v = heapq.heappop(pq)

    for cost, next_v in graph[cur_v]:
      next_cost = cost + cur_cost
      if next_cost < costs[next_v]:
        costs[next_v] = next_cost
        heapq.heappush(pq,(next_cost,next_v))

  answer = []
  for i, c in enumerate(costs):
    if 0< c <= k:
      answer.append(i)

  return answer



print(solution(13,	5,	[1,9]	,[[1,2,3],[2,4,4],[3,2,1],[1,6,6],[1,5,6],[1,7,6],[6,7,2],[5,7,5],[7,8,2],[9,7,3],[9,10,6],[9,11,3],[11,12,2],[11,13,4]]))
print(solution(7	,10	,[2]	,[[1,2,11],[1,5,1],[2,4,5],[5,4,4],[4,3,7],[4,6,8],[4,7,3],[6,7,3]]))