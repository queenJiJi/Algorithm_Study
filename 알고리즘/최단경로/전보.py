'''
아이디어
  * 통로 = 간선
  * 방향성이 있음
  * 거리가 가장 먼 값을 출력 = 도달 할 수 있는 가장 먼(max)노드와의 최단 거리 
  * 이 문제는 한도시에서 다른 도시까지의 최단 거리 문제로 치환 가능 -> 다익스트라알고리즘 사용

'''
import sys
import heapq
sys.stdin = open(
    '/Users/jiyeonpark/Desktop/Python/알고리즘/Algorithm_Study/알고리즘/최단경로알고리즘/input/전보.txt', 'r')
INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정
# n:도시의 개수(=노드개수), m: 통로의 개수(=간선 갯수), 시작노드
n, m, start = map(int, input().split())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for _ in range(n+1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)
# 모든 간선 정보를 입력받기
for _ in range(m):
    x, y, z = map(int, input().split())
    # x번 노드에서 y번 노드로 가는 비용이 z라는 의미
    graph[x].append((y, z))

# 다익스트라 함수


def dijkstra(start):
    # 큐 만들기
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    distance[start] = 0
    heapq.heappush(q, (0, start))
    # 큐가 비어있지 않다면
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보를 꺼내기
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            # 다른 노드까지의 cost 계산
            cost = dist + i[1]
        # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                # distance 리스트의 값 갱신
                distance[i[0]] = cost
                # 힙에 새로운 값과 해당 노드 갱신
                heapq.heappush(q, (cost, i[0]))


# 다익스트라 함수 실행
dijkstra(start)
# 도달할 수 있는 노드의 개수
count = 0
# 도달할 수 있는 노드 중에서, 가장 멀리 있는 노드와의 최단 거리
max_distance = 0
for d in distance:
    # 도달 할 수있는 노드인 경우
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

# 시작노드는 제외해야하므로 count-1출력
print(count-1, max_distance)
