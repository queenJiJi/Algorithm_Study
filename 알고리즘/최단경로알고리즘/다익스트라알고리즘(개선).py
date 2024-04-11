'''
  [ 개선된 다익스트라 알고리즘 ]
# 개선된 구현 방법 -> 우선순위 큐인 힙 자료구조를 사용
# 단계마다 '방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택' 하기 위해
  # '힙' 자료구조를 이용
# 다익스트라 알고리즘이 동작하는 '기본 원리는 동일'
  # 단, 현재 가장 가까운 노드를 저장해놓기 위해서 '힙 자료구조'를 추가적을 이용한다는 점이 다름
  # 현재의 최단 거리가 가장 짧은 노드를 선택해야하므로 '최소 힙'을 사용

# 힙 자료구조를 이용하는 다익스트라 알고리즘의 시간 복잡도: O(ElogV)
  # 노드를 하나씩 꺼내 검사하는 반복문(whlie문)은 노드의 개수 V이상의 횟수로는 처리되지 않습니다.
    # 결과적으로 현재 우선순위 큐에서 꺼낸 노드와 연결된 다른 노드들을 확인하는 총횟수는 최대 간선의 개수(E)만큼 연산이 수행 될 수 있음
  # 직관적으로 '전체 과정은 E개의 우너소를 우선순위 큐에 넣었다고 모두 빼내는 연산과 매우 유사'
    # 시간 복잡도를 O(ElogV)로 판단할 수 있음
'''
import heapq
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
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번노드에서 b번노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))

# 여기까진 이전 일반적인 다익스트라 알고리즘과 동일
  # 힙을 사용하니까 방문 여부를 확인할 리스트(visit) 필요없음
# 아래 다익스트라 알고리즘에서 변화됨


def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:  # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)  # dist: 거리값, now: 현재노드
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시(방문처리 리스트 필요없이)
        # 현재꺼낸 노드의 거리값이(dist) distance테이블에 기록된 값보다 더 클 경우
        if distance[now] < dist:
            continue  # 이미 처리가 된 것으로 간주할 수 있기 때문에 그냥 무시
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]  # i[1]:~까지 가는 거리 값
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:  # i[0]: ~갈 목표 노드
                distance[i[0]] = cost  # 더 짧은 거리로 갱신
                heapq.heappush(q, (cost, i[0]))


# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리르 출력
for i in range(1, n+1):
   # 도달 할 수 없는 경우 무한(infinity) 이라고 출력
    if distance[i] == INF:
        print('INFINITY')
    else:
        print(distance[i])
