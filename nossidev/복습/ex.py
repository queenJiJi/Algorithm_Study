import collections, heapq

def solution(n, edges, succProb, start, end):
  graph = collections.defaultdict(list)

  for i in range(len(edges)):
      edges[i].append(succProb[i])
  
  for a,b,w in edges:
      graph[a].append((w,b))
      graph[b].append((w,a))

  # print(graph)



  prob = [0.0]*n
  pq = [(-1.0,start)]
  prob[start] = 1.0
  while pq:
      cur_prob, cur_node = heapq.heappop(pq)
      # if prob[cur_node] > cur_prob:
      #     continue
      if cur_node == end:
          return prob[end]
      
      for probability, next_node in graph[cur_node]:
          next_probability = -probability*cur_prob
          if next_probability > prob[next_node]:
              prob[next_node] = next_probability
              heapq.heappush(pq,(-next_probability,next_node))
  # print(prob)
  # return prob[end_node]
  return 0
print(solution(n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2))
print(solution( n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2))
print(solution( n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2))