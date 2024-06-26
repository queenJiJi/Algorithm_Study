from collections import defaultdict
def solution(n, edges):
  graph = defaultdict(list)

  # 단방향 그래프 생성
  for u,v in edges:
    graph[u].append(v) 

  # dfs 재귀함수로 순회
  def dfs(cur_node):
    # 다음에 감염될 노드들의 집합 
    child_node = set()
    for node in cur_node:
      for child in graph[node]:
        child_node.add(child)
    result = len(cur_node)
    if child_node:
      min_dfs_result = float('inf')
      # 다음 노드 중 하나를 제외하고 재귀함수 호출(간선 하나를 잘랐다 했을 때)
      for child in child_node:
        min_dfs_result = min(min_dfs_result, dfs(child_node-set([child])))
      # 호출 결과 중 가장 작은 값을현재 층의 노드수에 더해 반환
      result += min_dfs_result
    return result
  return dfs(set([0])) # 루트노드부터 바이러스 시작이니 루트노드부터 탐색 시작 


print(solution(19,[[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [2, 6], [3, 7], [3, 8], [3, 9], [4, 10], [4, 11], [5, 12], [5, 13], [6, 14], [6, 15], [6, 16], [8, 17], [8, 18]]))
print(solution(14,[[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [2, 7], [3, 8], [3, 9], [3, 10], [4, 11], [4, 12], [4, 13]]))
print(solution(10,[[0, 1], [0, 2], [1, 3], [2, 4], [2, 5], [2, 6], [3, 7], [3, 8], [3, 9]]))


