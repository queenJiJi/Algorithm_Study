import collections, heapq
def solution(n,edges, succProb,start,end):
  graph = collections.defaultdict(list)

  for i in range(len(edges)):
    edges[i].append(succProb[i])
  
  for u,v,w in edges:
    graph[u].append([w,v])
    graph[v].append([w,u])
  
  pq=[(-1.0,start)]
  prob =[0.0]*n
  prob[start] = 1.0

  while pq:
    cur_prob, cur_v = heapq.heappop(pq)

    if cur_v == end:
      return prob[end]
    
    for probability, next_v in graph[cur_v]:
      next_prob = -probability*cur_prob

      if next_prob > prob[next_v]:
          prob[next_v] = next_prob
          heapq.heappush(pq,(-next_prob,next_v))
  return 0




print(solution(n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2))
print(solution( n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2))
print(solution( n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2))