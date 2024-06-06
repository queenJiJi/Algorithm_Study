import heapq, collections
def solution(n,edges,succProb,start,end):

  graph = collections.defaultdict(list)

  for i in range(len(edges)):
    edges[i].append(succProb[i])
  
  for a,b,w in edges:
    graph[a].append((w,b))
    graph[b].append((w,a))


  prob = [0.0]*n
  pq = [(-1.0,start)] # 0 부터시작하면 곱했을 때 계속해서 0이 나오니까 -1로 초기화해줘야함 (1이 아닌 이유는 maxheap 구현을 위해 부호 반대로)
  prob[start] = 1.0 # prob결과는 양수니까 양수로 초기화

  while pq:
    cur_prob, cur_node = heapq.heappop(pq)
    # print(cur_prob,cur_node)

    # if prob[cur_node] > cur_prob:
    #   continue
    if cur_node == end: # 현재 노드가 도착지 노드라면 결과반환
      return prob[end]
    
    for probability, next_node in graph[cur_node]:
      next_probability = -cur_prob * probability # maxheap구현을 위해 부호 반대로 
      if next_probability > prob[next_node]:
        prob[next_node] = next_probability
        heapq.heappush(pq,(-next_probability,next_node)) # 다시 큐에 넣을 때는 원상복구시키기 (위에서 어짜피 다시 음수 만들어주니까)
  # print(prob)
  # return prob[end]
  return 0



print(solution(n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2))
print(solution( n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2))
print(solution( n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2))

