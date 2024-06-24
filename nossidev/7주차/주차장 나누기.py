from collections import defaultdict
def solution(n, cars, links):
  graph = defaultdict(list)
  cars_sum = [0]+cars # 1부터 시작해야하니까 0엔 0 넣어주고 extend // [0,22,9,1,...]

  for u,v in links:
    graph[u].append(v)
    graph[v].append(u)
  print('hi',graph[1].pop())

  visited = [False for _ in range(len(cars)+1)]
  visited[1] = True
  
  # 스택에 루트노드를 넣고 dfs진행
  stack = [1]
 
  while stack:
    # 스택에 추가하려는 노드가 부모 노드인 경우 제거(이미 visited한 것을 또 visit하면 안되니까)
    if graph[stack[-1]] and visited[graph[stack[-1]][-1]]:
      graph[stack[-1]].pop()
    # 자식 노드가 있는 경우 스택에 다음 노드를 추가
    if graph[stack[-1]]: # 아직 방문은 안한 것
      tmp = graph[stack[-1]].pop()
      visited[tmp] = True
      stack.append(tmp)
    # 자식노드가 없는 경우 - 해당 노드의 노드값을 부모 노드에 추가
    else:    
      tmp = stack.pop()
      if stack:
        cars_sum[stack[-1]] += cars_sum[tmp]
  target = cars_sum[1] /2 # 루트노드에 저장되어있는 총 자동차갯수 합 //2
  answer = target
  # 노드에 저장된 차량의 수들 중 가장 target값과 차이가 없는 최솟값 찾기
  for cars_per_node in cars_sum:
    answer = min(answer, abs(target-cars_per_node))

  return int(answer*2)


print(solution(13,	[22,9,1,15,8,6,20,7,11,5,10,4,1],	[[4,7],[13,10],[6,3],[7,1],[6,12],[5,11],[5,6],[5,10],[9,8],[8,11],[8,2],[7,8]]))
print(solution(6,	[6,4,10,9,8,4],	[[4,1],[3,2],[1,6],[3,5],[5,1]]))     
