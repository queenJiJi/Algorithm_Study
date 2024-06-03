import heapq, collections
def solution(times,n,k):

  # 인접리스트로 그래프 구성
  graph = collections.defaultdict(list)


  for time in times:
    graph[time[0]].append((time[2],time[1]))
  # print(graph)

  # 해당 그래프에 다익스트라 알고리즘 적용
  costs = {}
  pq = [(0,k)]

  while pq:
    cur_cost, cur_v = heapq.heappop(pq)

    if cur_v not in costs:
      costs[cur_v] = cur_cost
      for cost, next_v in graph[cur_v]:
        next_cost = cur_cost + cost
        heapq.heappush(pq,(next_cost,next_v))

  #  모든 노드를 다 돌았는지 확인
  for node in range(1,n+1):
    if node not in costs:
      return -1
  return max(costs.values()) 



print(solution(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2))
print(solution(times = [[1,2,1]], n = 2, k = 1))
print(solution(times = [[1,2,1]], n = 2, k = 2))