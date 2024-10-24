import sys
input = sys.stdin.readline

R, C = map(int, input().rstrip().split())
board = [list(input().rstrip()) for _ in range(R)]
answer = 0
saving = set()

def dfs(r, c, cnt):
    global answer
    answer = max(answer, cnt)

    for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        nr, nc = r + dx, c + dy

        # 경계 체크 및 알파벳 중복 여부 확인
        if 0 <= nr < R and 0 <= nc < C and board[nr][nc] not in saving:
            saving.add(board[nr][nc])  # 방문 처리
            dfs(nr, nc, cnt + 1)  # 다음 칸으로 이동
            saving.remove(board[nr][nc])  # 백트래킹

# 시작점 처리
saving.add(board[0][0])
dfs(0, 0, 1)

print(answer)