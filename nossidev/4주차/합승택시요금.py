import collections, heapq

#✅ 인풋을 본인이 쓰기 편한 구조로 바꾸기(다익스트라) => 무방향 그래프 만들기

#✅ s, a, b 3개의 노드에서 모든 노드까지 도달하는 최소 비용을 저장한다.
	#✅ case1: s, a, b 3개의 노드에서 각각 다익스트라 알고리즘을 수행한다.
#✅ 모든 노드를 순회하며 cost(s->x) + cost(x->a) + cost(x->b)의 최소비용을 반환한다.

def solution(n,s,a,b,fares):
  graph = collections.defaultdict(list)

  for i,j,f in fares:
    graph[i].append((f,j))
    graph[j].append((f,i))
  
  costs = [[float('inf')]*(n+1) for _ in range(3)]
  answer = float('inf')

  # s,a,b 3개의 노드에서 각각 다익스트라 알고리즘 수행
  for i, start_node in enumerate((s,a,b)):
    pq = []
    heapq.heappush(pq,(0,start_node))
    costs[i][start_node] = 0

    while pq:
      cur_cost,cur_v = heapq.heappop(pq)

      for cost,next_v in graph[cur_v]:
        next_cost = cost+cur_cost
        if costs[i][next_v] > next_cost:
          costs[i][next_v] = next_cost
          heapq.heappush(pq,(next_cost, next_v))
  # 모든 노드를 순회하면서 cost(s->x) + cost(x->a) + (cost(x->b)의 최소비용 반환 
  print(costs)
  for i in range(1,n+1):
    answer = min(answer, costs[0][i]+costs[1][i]+costs[2][i])    
  return answer 



print(solution(6,	4,	6,	2,	[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
print(solution(7,	3,	4,	1,	[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
print(solution(6,	4,	5,	6,	[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]))
