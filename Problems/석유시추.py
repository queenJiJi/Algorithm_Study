from collections import deque


def solution(land):
    answer = 0
    n, m = len(land), len(land[0])

    # 방문배열
    visited = [[False] * m for _ in range(n)]
    # 각 열의 기름의 총량을 저장하는 리스트
    oil = [0] * m
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    def bfs(row, col):
        queue = deque()
        queue.append([row, col])
        visited[row][col] = True
        cnt = 1
        # bfs 탐색중 석유가 있는 열, 중복을 방지하기 위한 set
        oil_covered = {col}

        while queue:
            pr, pc = queue.popleft()
            for dr, dc in directions:
                nr, nc = pr + dr, pc + dc
                if 0 <= nr < n and 0 <= nc < m and land[nr][nc] == 1 and not visited[nr][nc]:
                    queue.append([nr, nc])
                    visited[nr][nc] = True
                    cnt += 1
                    # 현재 석유를 발견한 열 추가
                    oil_covered.add(nc)

        # 각 열을 돌면서 석유량 추가
        for c in oil_covered:
            oil[c] += cnt

    # bfs 탐색
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:
                bfs(i, j)

    answer = max(oil)

    return answer

print(solution([[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]))
print(solution([[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]]))
