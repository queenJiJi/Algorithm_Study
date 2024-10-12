# 컵이동문제
# def solution(cups, moves):
#     # 각 이동에서 구슬을 이동시키는 작업
#     for move in moves:
#         a, b = move[0] - 1, move[1] - 1  # 1-based index를 0-based로 변환
#         cups[b] += cups[a]  # a번 컵의 구슬을 b번 컵으로 모두 옮김

#     return cups
# print(solution([4, 3, 2, 1],[[3, 2], [2, 1], [4, 1]]))
# print(solution([2, 3, 3, 4, 5],[[1, 2], [2, 3], [4, 5], [2, 4], [1, 3]]))

# 블록 문제
from collections import deque

def solution(board, requests):
    rows, cols = len(board), len(board[0])
    board = [list(row) for row in board]  # 문자열을 2D 배열로 변환
    to_remove = [[False for _ in range(cols)] for _ in range(rows)]  # 제거할 칸 표시

    # 상하좌우 탐색을 위한 방향 벡터
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def is_on_edge(r, c):
        """해당 좌표가 보드의 가장자리에 있는지 확인"""
        return r == 0 or r == rows - 1 or c == 0 or c == cols - 1

    def bfs(r, c, char):
        """BFS로 외부와 연결된 해당 문자를 제거"""
        queue = deque([(r, c)])
        cluster = [(r, c)]
        to_remove[r][c] = True
        is_edge = is_on_edge(r, c)

        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and not to_remove[nx][ny] and board[nx][ny] == char:
                    queue.append((nx, ny))
                    cluster.append((nx, ny))
                    to_remove[nx][ny] = True
                    if is_on_edge(nx, ny):
                        is_edge = True

        # 외부에 맞닿아 있지 않고 연속된 문자인 경우 모두 제거
        if not is_edge and char in requests:
            for x, y in cluster:
                to_remove[x][y] = True

    # 1. 외부에 있는 문자부터 BFS로 탐색하여 제거
    for r in range(rows):
        for c in range(cols):
            if board[r][c] in requests and not to_remove[r][c]:
                bfs(r, c, board[r][c])

    # 2. 남은 칸 계산
    remaining_cells = 0
    for r in range(rows):
        for c in range(cols):
            if not to_remove[r][c]:
                remaining_cells += 1

    return remaining_cells

# 테스트 실행
board = ["ABCD", "XYBJ", "ABBC", "XABC"]
requests = ['A', 'B', 'BB', 'C']
print(solution(board, requests))  # 결과: 6