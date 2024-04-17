import sys
sys.stdin = open(
    '/Users/jiyeonpark/Desktop/Python/알고리즘/Algorithm_Study/알고리즘/구현:시뮬레이션과 완전탐색/input/게임개발.txt', 'r')
n, m = map(int, input().split())  # n: 세로, m: 가로
a, b, d = map(int, input().split())  # 캐릭터가 있는 좌표: (A,B), d: 바라보는 방향
# 방향값 : d = [0,1,2,3] == ['북','동','남','서']
# board = []
# for _ in range(n):
#     board.append(list(map(int, input().split())))
# print(board)

board = [list(map(int, input().split())) for _ in range(n)]
print(board)

# 0: 육지, 1:바다
# 맵의 외곽은 항상 바다임(a,b = n,m이면) 못감
'''
캐릭터는 동서남북 중 한 곳을 바라본다.
캐릭터는 상하좌우로 움직이며, 바다에는 갈 수 없다.
# 캐릭터의 움직임
# 현재 방향을 기준으로 왼쪽 방향(반시계 90º 회전)부터 갈 곳을 정한다.
  # 바라본 위치가 아직 가보지 못한 곳이라면 바라보는 방향으로 전진한다.
  # 바라본 방향에 가보지 못한 곳이 없다면 1단계로 돌아간다.
# 만약 네 방향 모두 가본 칸이거나 바다로 되어 있는 칸이면, 
# 바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로 돌아간다.
  # 뒤쪽 방향이 바다라면 움직임을 멈춘다.
# 메뉴얼에 따라 캐릭터를 이동시킨 뒤에 캐릭터가 방문한 칸의 수를 출력하라.
'''

r, c = a, b
board[r][c] = 1  # 시작점은 방문처리
dir = d
# dir = [0, 1, 2, 3]  # 바라보는 방향 : 북,동,남,서
# 북, 동, 남, 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
count = 1  # 이동한 칸의 갯수
dir_count = 0

while True:
    dir -= 1
    if dir < 0:
        dir = 3

    nr = r + dr[dir]
    nc = c + dc[dir]
    # 4번동안 반복
    if board[nr][nc] == 0:  # 바로 왼쪽 방향에 0이 있으면 d 왼쪽으로 회전, 왼쪽 한칸 전진
        board[nr][nc] = 1
        r, c = nr, nc
        count += 1
        dir_count = 0
    else:  # 바로 왼쪽 방향에 0이 없으면 d 왼쪽으로 회전
        dir_count += 1

    if dir_count == 4:  # 4번 반복 후에도 갈곳이 없다면 뒤로 한칸 후진
        nr = r-dr[dir]
        nc = c-dc[dir]

        if board[nr][nc] == 0:  # 후진 할 수 있으면 1단계 다시 진행
            # 1단계 다시 진행 # 가본 칸은 바다로 변경, count추가
            r, c = nr, nc
            board[nr][nc] = 1
            count += 1
            dir_count = 0
        else:  # 후진 할 수 없으면 종료
            break

print(count)
for i in board:
    print(*i)
