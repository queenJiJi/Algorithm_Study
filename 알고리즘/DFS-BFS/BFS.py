# BFS 소스코드 예제

# step0: BFS는 큐를 사용하니까 큐를 위한 덱 라이브러리 호출
from collections import deque

# step1: 각 노드가 연결된 정보를 2차원 리스트로 정의
graph = [
    [],  # list는 0부터 시작하는데, 노드0은 없으니까 비워두기
    [2, 3, 8],  # 노드 1(최상단노드)에 연결되어있는 노드
    [1, 7],  # 노드 2에 연결되어있는 노드들
    [1, 4, 5],  # 노드 3에 연결되어있는 노드들
    [3, 5],  # 노드 4에 연결되어있는 노드들
    [3, 4],  # 노드 5에 연결되어있는 노드들
    [7],  # 노드 6에 연결되어있는 노드들
    [2, 6, 8],  # 노드 7에 연결되어있는 노드들
    [1, 7],  # 노드 8에 연결되어있는 노드들
]

#  노드가 방문된 정보를 1차원 리스트로 표현
# 즉, 방문정보를 저장한 리스트
# 초기화 값은 일단 아무것도 방문하지 않았으니 false로 시작 9=(노드갯수+1)-노드0이포함되어있으니까
visited = [False] * 9

# BFS 메서드 정의


def bfs(graph, start, visited):  # start:시작노드(=최상단노드)
    # 큐(queue) 구현을 위해 deque 라이브러리 활용
    # 큐 선언
    queue = deque([start])  # 첫 시작노드를 큐에 넣는 것으로 초기화
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 노드(원소)를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')

        # 아직 방문하지 않은 인접한 원소(노드)들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:  # 방문하지 않았다면
                queue.append(i)  # 큐에 삽입
                visited[i] = True  # 방문 처리


# 정의된 DFS함수 호출
bfs(graph, 1, visited)
