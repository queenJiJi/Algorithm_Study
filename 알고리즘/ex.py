n = 4

A = [[0] * n for _ in range(n)]

# 상 하 좌 우
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
count = 1
r, c = 0, 0
dir_idx = 0

while count <= n * n:
    # 현재 위치에 숫자 채우기
    A[r][c] = count

    # 다음 위치 계산
    nr = r + dr[dir_idx]
    nc = c + dc[dir_idx]

    # 다음 위치가 범위를 벗어나거나 이미 숫자가 채워진 경우 방향 전환
    if nr < 0 or nc < 0 or nr >= n or nc >= n or A[nr][nc] != 0:
        dir_idx = (dir_idx + 1) % 4
        nr = r + dr[dir_idx]
        nc = c + dc[dir_idx]

    # 다음 위치로 이동
    r, c = nr, nc
    count += 1

# 배열 출력
for row in A:
    print(*row)
