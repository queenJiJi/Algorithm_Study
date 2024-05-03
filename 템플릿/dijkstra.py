'''
  우선순위 큐 = 힙(자료구조) -- 자동으로 우선순위가 높은 순서대로(비용이 가장 작은것) 정렬 해줌 
                          <-> 반대로 우선순위가 낮은순서대로(비용이가장 높은것) 정렬하고 싶으면 그냥 모든 노드에 '-1'을 곱해주면 됩 
    heapq.heappush(어디에, 무엇을 )
    heapq.heappop(어디에서)

  다익스트라알고리즘: 가중치 그래프에서 가장 빠른 노선/ 비용이 가장 적은 루트 찾을때 사용 
    (비가중치 그래프에선 BFS 알고리즘 사용)

  다익스트라 구현 순서:
    1. 우선순위큐에 시작노드 추가
      2. 우선순위가 가장 높은 노드 추출
      3. 방문여부 확인 
        4. 비용 업데이트
        5. 현재 노드와 연결된 모든 노드들을 우선순위 큐에 추가
    6. 목적지에 기록된 비용 반환 
'''
import heapq

# graph [(비용, 노드), (비용 노드)]
graph = {
    1: [(2, 2), (1, 4)],  # 1번 노드에 2,4번 노드들이 연결되어있으며 2번까지 가는 비용은 2, 4번까지의 비용은 1임
    2: [(1, 3), (9, 5), (6, 6)],
    3: [(4, 6)],
    4: [(3, 3), (5, 7)],
    5: [(1, 8)],
    6: [(3, 5)],
    7: [(7, 6), (9, 8)],
    8: []
}


def dijkstra(graph,start,final):
  costs = { } # 각 노드까지 가는 비용을 업데이트 해주기 위해서
  pq = [] # 우선순위 큐
  heapq.heappush(pq, (0,start)) # 1. 우선순위큐에 시작노드 추가

  while pq: # 우선순위 큐가 빌때까지
    cur_cost, cur_v = heapq.heappop(pq) # 2. 우선순위가 가장 높은 노드 추출
    if cur_v not in costs: # 3. 방문하지 않은 노드라 cost에 거기까지의 비용이 업데이트 되어있지 않다면
      costs[cur_v] = cur_cost # 4.costs딕셔너리에 시작부터 현재노드까지의 비용 업데이트
      for cost, next_v in graph[cur_v]: # 5.현재 노드와 연결된 모든 노드들을 우선 순위 큐에 추가
        next_cost = cur_cost+cost
        heapq.heappush(pq, (next_cost, next_v)) # 힙에 넣음으로써 우선순위 순서대로 자동 정렬
  return costs[final] # 6


print(dijkstra(graph,1,8))
 







