'''
1. 우선순위큐에 시작노드 추가
  2. 우선순위가 가장 높은 노드추출
  3. 방문여부 확인
    4. 비용업데이트
    5. 현재 노드와 연결된 노드들을 우선순위 큐에 추가 
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

# distance를 리스트로 구현했을 시(그래프가 숫자노드일 경우)
def dijkstra_list(graph,start_node,dest,n):
  distance = [float('inf')] * (n+1) # 노드가 0이 아닌 1부터 시작이니까 (n+1)
  pq = [(0,start_node)] # 1. 우선순위큐에 시작노드 추가

  while pq:
    cur_dist, cur_node = heapq.heappop(pq)
    if distance[cur_node] < cur_dist: # 만약 미리 저장되어있는 최단 거리 값보다 지금 계산해온 거리가 더 크다면 다음거로 넘어감(이미 작은 값이 저장되어있으니 업데이트 필요없음)
      continue   
  
    for cost, next_node in graph[cur_node]: # 현재노드와 연결된 노드들 확인
      next_dist = cur_dist + cost # 현재노드까지의 거리 저장된것 + 다음 노드까지의 거리
      if next_dist < distance[next_node]: # 다음 노드까지의 계산된 거리가 이미 저장되어있던 최소거리보다 작으면 
        distance[next_node] = next_dist # 새로운 최소거리비용으로 업데이트 
      heapq.heappush(pq, (next_dist,next_node)) # 큐에 연결된 다음 노드들 넣어주기
  print(distance)
  return distance[dest] # 목적지까지의 저장된 최소비용 반환

# distance를 dictionary로 구현했을 시(그래프가 어떤 식으로 나와도 사용 가능)
def dijkstra_dic(graph,start_node,dest,n):
  distance = {}
  pq = [(0,start_node)]

  while pq:
    cur_dist, cur_v = heapq.heappop(pq)

    if cur_v not in distance:
      distance[cur_v] = cur_dist

      for cost,next_v in graph[cur_v]:
        next_dist = cur_dist + cost
        heapq.heappush(pq, (next_dist,next_v))
  print(distance)
  return distance[dest]



print(dijkstra_list(graph,1,8,len(graph)))
print(dijkstra_dic(graph,1,8,len(graph)))
