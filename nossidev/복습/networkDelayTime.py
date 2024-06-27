# 가중치 그래프 - 다익스트라 알고리즘 구현 : 그때 그때 최적의 선택 (최대 힙 구현)
import heapq, collections

def solution(times, n, k ):
  # k: 시작노드 

  graph = collections.defaultdict(list)

  for time in times:
    graph[time[0]].append((time[2],time[1]))

  costs = {}
  pq = [(0,k)]

  while pq:
    cur_cost, cur_v = heapq.heappop(pq)
    
    if cur_v not in costs:
      costs[cur_v] = cur_cost
      for cost, next_v in graph[cur_v]:
        next_cost = cur_cost + cost
        heapq.heappush(pq,(next_cost,next_v))
  
  for node in range(1,n+1):
    if node not in costs:
      return -1
  return max(costs.values())

print(solution(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2))
print(solution(times = [[1,2,1]], n = 2, k = 1))
print(solution(times = [[1,2,1]], n = 2, k = 2))