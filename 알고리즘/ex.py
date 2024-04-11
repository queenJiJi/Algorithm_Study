
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for _ in range(5)]

# 모든 간선 정보를 입력받기
for _ in range(4):
    a, b, c = map(int, input().split())
    # a번노드에서 b번노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))

print(graph)
