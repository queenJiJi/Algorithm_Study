import sys
from collections import deque
sys.stdin = open('알고리즘/DFS-BFS/input/특정거리의도시찾기.txt', 'r')

# n: 도시갯수, m:도로갯수, k: 거리정보, x: 출발도시
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]


# 모든 도로 정보 입력받기
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (n+1)
distance[x] = 0  # 출발도시까지의 거리는 0으로 설정

# BFS 수행
q = deque([x])  # 출발 도시/노드(x) 넣어주고 시작
while q:  # 큐가 빌때까지 반복
    now = q.popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next_node in graph[now]:
        # print(next_node)
        # 아직 방문하지 않은 도시라면
        if distance[next_node] == -1:
            # 최단거리 갱신
            distance[next_node] = distance[now] + 1
            q.append(next_node)

# 최단 거리가 k인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True

# 만약 최단 거리가 K인 도시가 없다면, -1 출력
if check == False:
    print(-1)
