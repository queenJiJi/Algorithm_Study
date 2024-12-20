# 해당 문제는 BFS를 활용해서 풀어야함
# BFS는 시작지점에서 "가까운 노드부터 차례대로" 그래프의 모든 노드를 탐색
# bfs는 노드간 거리가 모두 같을때, 최단거리를 찾아주는 알고리즘
# 상,하,좌,우로 연결된 모든 노드로의 거리가 1로 동일
# 따라서 (1,1)지점부터 bfs를 수행하여 모든 노드의 최단 거리 값을 기록하면 해결 가능

# 괴물 있는 부분 : 0  없는 부분: 1, 미로를 탈출하기 위한 '최소 칸의 개수'
# (1,1)에서 (n,m)으로 갈 수 있는 최단 거리 구하라는 것

# 프로그래머스 미로탈출(LV2)도 풀어보기
#  https://he-ya.tistory.com/105
import sys
from collections import deque
sys.stdin = open('알고리즘/DFS-BFS/input/미로탈출문제.txt', 'r')

# n,m을 공백을 기준으로 구분하여 입력받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
# print(graph)

# 이동할 네가지 방향 정의(상,하,좌,우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# bfs소스코드 구현


def bfs(x, y):
    # 큐 구현을 위해 deque라이브러리 사용
    queue = deque()
    queue.append((x, y))  # 첫 초기값 넣고 시작

    # 큐가 빌때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향으로 위치 확인
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            # 미로찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽(0)인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n-1][m-1]


print(bfs(0, 0))
