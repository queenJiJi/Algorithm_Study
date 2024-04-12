import sys
sys.stdin = open(
    '/Users/jiyeonpark/Desktop/Python/알고리즘/Algorithm_Study/알고리즘/최단경로알고리즘/input/다익스트라.txt', 'r')
INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for _ in range(n+1)]
# 방문한 적이 있는지 체크하는 목적의 리스트 만들기
visited = [False] * (n+1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번노드에서 b번노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))


def get_smallest_node():  # 방문하지 않는 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
    min_value = INF
    index = 0  # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True

    for j in graph[start]:
        # 특정 노드부터 목표 노드(j[0])까지의 거리(j[1])를 distance테이블에 생성
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost  # 더 짧은 값으로 갱신


# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단거리를 출력
for i in range(1, n+1):
    # 도달할 수 없는 경우, 무한(INF)이라고 출력
    if distance[i] == INF:
        print('INFINITY')
    else:
        print(distance[i])

# 총 O(V)번에 걸쳐서 최단 거리가 가장 짧은 노드를 매번 '선형 탐색'해야 함
# 따라서 전체 시간 복잡도는 O(V^2) 입니다
# 일반적으로 코딩테스트의 최단 경로 문제에서 전체 노드의 개수가 5000개 이하라면 이 코드로 문제를 해결 할 수 있음
# 하지만 노드의 개수가 10000개를 넘어가는 문제라면? => '우선순위 큐' 자료구조를 사용해야함
