### 그래프 ###
def solution(cups,moves):
  n = len(cups)
  parent = [None] * n

  for move in moves:
    a,b = move
    parent[a-1] = b-1

  children = [[] for _ in range(n)]

  for child, p in enumerate(parent):
    if p is not None:
      children[p].append(child)

  answer = [0] * n
  def dfs(node):
    answer[node] = cups[node]

    for child in children[node]:
      answer[node] += dfs(child)

    return answer[node]
  
  for i in range(n):
    if parent[i] is None:
      dfs(i)

  return answer

print(solution([4, 3, 2, 1],[[3, 2], [2, 1], [4, 1]]))
print(solution([2, 3, 3, 4, 5],[[1, 2], [2, 3], [4, 5], [2, 4], [1, 3]]))