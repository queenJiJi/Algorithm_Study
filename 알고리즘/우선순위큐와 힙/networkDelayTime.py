import heapq
from collections import defaultdict
times = [[2,1,1],[2,3,1],[3,4,1]]

'''
구현순서: 
1. 그래프 구현
2. 다익스트라 알고리즘 구현
  3. 방문하지 않은 노드 반환
4. 모든 costs들 중 최대값 반환
'''




def solution(times,n,k):
  # 1.
  graph = defaultdict(list)
  for time in times:
    graph[time[0]].append((time[2],time[1]))

  #2 
  costs = {}
  pq = []
  heapq.heappush(pq,(0,k))

  while pq:
    cur_cost, cur_v = heapq.heappop(pq)
    if cur_v not in costs:
      costs[cur_v] = cur_cost
      for cost, next_v in graph[cur_v]:
        next_cost = cur_cost + cost
        heapq.heappush(pq,(next_cost, next_v))

  print(costs)
  # 3.
  for i in range(1,n+1):
    if i not in costs:
      return -1
    
  #4
  return max(costs.values())


print(solution(times,4,2))