'''
아이디어
* k를 거쳐서 가는데, N의 최대 길이가 100이므로 플로이드 워셜 알고리즘 이용가능
# 핵심 아이디어: 전형적인 최단 거리 문제이므로 '최단 거리 알고리즘'을 이용해 해결
# 플로이드 워셜 알고리즘을 수행한 뒤에 
(1번 노드에서 X까지의 최단 거리 + X에서 K까지의 최단 거리)를 계산하여 출력하면 정답
'''

import sys
sys.stdin = open(
    '/Users/jiyeonpark/Desktop/Python/알고리즘/Algorithm_Study/알고리즘/최단경로알고리즘/input/미래도시.txt', 'r')
INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정
n, m = map(int, input().split())  # n:노드 수, m: 경로갯수
# 2차원 리스트(그래프 표현)을 만들고, 모든 값을 무한으로 초기화
graph = [[INF]*(n+1) for _ in range(n+1)]
# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for i in range(n+1):
    for j in range(n+1):
        if i == j:
            graph[i][j] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    a, b = map(int, input().split())
    # A와 B가 서로에게 가는 비용은 1이라고 설정
    graph[a][b] = 1
    graph[b][a] = 1

# 거쳐갈 노드 k와 최종 목적지 노드 x를 입력받기
x, k = map(int, input().split())
# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(n+1):
    for a in range(n+1):
        for b in range(1+n):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

# 수행된 결과를 출력
distance = graph[1][k] + graph[k][x]

# 도달할 수 없는 경우, -1을 출력
if distance >= INF:
    print(-1)
# 도달할 수 있는 경우, 최단 거리 출력
else:
    print(distance)
