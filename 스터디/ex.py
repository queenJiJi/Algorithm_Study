from collections import deque
import sys

N= int(input())
board=[list(map(int,sys.stdin.readline().strip().split())) for _ in range(N)]
ans = 0
size=2 # 아기상어의 초기 크기
ans, cnt = 0,0 # 최소거리, 물고기를 잡아먹은 수 
locx,locy= 0,0 # 아기상어의 위치

def bfs(r,c, size):
    q=deque()
    visited = [[-1 for _ in range(N)] for _ in range(N)] # 방문처리 겸 방문거리 업데이트
    cases = [] # 먹을 수 있는 물고기들 
    q.append([r,c])

    visited[r][c]=0 # 현 위치 방문 처리

    while q:
        cur_r,cur_c=q.popleft()

        for dr,dc in [[-1,0],[0,1],[0,-1],[1,0]]:
            nr,nc =dr+cur_r, dc+cur_c
            if 0<=nr<N and 0<=nc<N and visited[nr][nc]==-1:
                if board[nr][nc] <= size: # 지나갈수있을 때 
                    q.append([nr,nc])
                    visited[nr][nc] = visited[cur_r][cur_c]+1 # 사이즈를 함께 저장 

                    if board[nr][nc]<size and board[nr][nc]!=0: # 먹을 수 있을 때
                        cases.append([nr,nc,visited[nr][nc]])
    return cases

# 아기상어의 현재위치
for r in range(N):
    for c in range(N):
        if board[r][c] == 9:
            locx,locy= r,c
            board[r][c] = 0 # 거기서부터 다시 움직이니까 0으로 초기화
# 물고기를 다 먹을때까지 무한 루프
while True:
    cases = bfs(locx,locy,size)

    # 먹을 수 있는 물고기가 없을 경우 종료
    if len(cases)==0:
        break

    # 먹을 수 있는 물고기가 있는 상태라면 위쪽부터->왼쪽 부터 = 행->열 정렬
    cases.sort(key=lambda x: (x[2],x[1],x[0])) #x[2]:행(row), x[1]:열(col), x[0]: 사이즈
    # 정렬된 결과값 중 가장 가까이 있는 물고기로 가기
    nx,ny,dist = cases[0]
    ans+=dist # 1칸당 시간 1초

    board[locx][locy], board[nx][ny] = 0,0 #먹었으니까 해당 위치 초기화
    locx,locy = nx,ny # 먹은 물고기 좌표로 아기상어 이동

    cnt+=1# 물고기를 먹었으니 먹은 물고기 갯수 추가

    if cnt == size:
        size+=1
        cnt=0
print(ans)
