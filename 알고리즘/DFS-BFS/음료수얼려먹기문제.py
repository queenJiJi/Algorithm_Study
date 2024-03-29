# 문제해결아이디어
# DFS/BFS로 해결가능하며,
#  0을 방문가능한 노드 , 1을 방문 불가능한 노드로 간주
#  그리고 0끼리 연결하면 그래프 형태로 나타낼 수 있음

# DFS를 활용하는 알고리즘은 다음과 같음:
# 1. 특정한 지점의 주변 상,하,좌,우를 살표본 뒤에 주변 지점 중에서
#    값이 '0'이면서 아직 방문하지 않은 지점이 있다면 해당 지점 방문
# 2. 방문한 지점에서 다시 상,하,좌,우를 살표보면서 방문을 진행하는 과정을 반복
#      하면, '연결된 모든 지점을 방문' 할 수 있음
# 3. 모든 노드에 대하여 1번과 2번 과정을 반복하며, 방문하지 않은 지점의 수를 카운트


n, m = map(int, input().split())
# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# DFS로 특정 노드를 방문하고 연결된 모든 노드들도 방문


def dfs(x, y):
    # 주어진 범위를 벗어나는 경우 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상,하,좌,우의 위치들도 모두 재귀적으로 호출
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False


# 모든 노드(위치)에 대하여 음료수 채우기
count = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS수행
        if dfs(i, j) == True:
            count += 1
print(count)
