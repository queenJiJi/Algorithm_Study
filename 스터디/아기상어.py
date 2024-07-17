import sys
from collections import deque

N= int(sys.stdin.readline().strip())
board=[list(map(int,sys.stdin.readline().strip().split())) for _ in range(N)]
ans = 0
shark_size = 2 # 상어 사이즈
cnt = 0 # 먹은 물고기 수 
cur_x, cur_y = 0,0 # 상어의 위치

# 가장 가까운 물고기의 위치를 찾는 bfs
def bfs(r,c,size):
    q=deque()
    q.append([r,c])
    visited=[[-1 for _ in range(N)] for _ in range(N)] # 방문 처리 및 거리 저장용
    cases= [] # 물고기를 먹을 수 있는 조건들 넣는 리스트
    visited[r][c] = 0 # 현재 위치 방문처리 
    
    while q:
        cur_r,cur_c =q.popleft()
        
        for dr,dc in [[-1,0],[0,1],[0,-1],[1,0]]:
            nr,nc = cur_r+dr, cur_c+dc
            if 0<=nr<N and 0<=nc<N and visited[nr][nc]==-1:
                if board[nr][nc]<=size: # 지나갈 수 있다면
                    q.append([nr,nc])
                    visited[nr][nc] = visited[cur_r][cur_c] +1
                    if board[nr][nc]<size and board[nr][nc]!=0: # 물고기를 먹을 수 있다면
                        cases.append([nr,nc,visited[nr][nc]])
    return cases
            

# 상어의 위치 찾기
for r in range(N):
    for c in range(N):
        if board[r][c] == 9:
            cur_x, cur_y = r,c
            board[r][c] = 0 # 상어가 처음 있던 위치 초기화
 

# 물고기 잡아먹기 - 잡아먹을 물고기가 없을 때까지 반복하는 무한루프
while True:
    cases = bfs(cur_x,cur_y,shark_size) # 먹을 물고기들

    if len(cases) == 0: # 더이상 먹을 물고기가 없다면
        break

    # 먹을 물고기를 발견했다면
    cases.sort(key=lambda x:(x[2],x[0],x[1])) # 가장가까운것-> 위쪽(r)물고기부터-> 왼쪽(c)물고기 (거리가까울수록->행이 작을수록->열이 작을수록)로 정렬
    nx,ny, dist = cases[0] # 다음 갈 위치와 거리
    ans += dist # 해당 거리까지 가야하니까 정답에 넣어주기

    cur_x,cur_y = nx,ny # 상어의 위치 이동
    board[cur_x][cur_y] = 0 # 먹은 그 위치 초기화(먹었으니까)

    cnt+=1 # 먹은 물고기 수 증가

    if shark_size == cnt: # 먹은 물고기 수와 상어의 크기가 같다면
        shark_size+=1 # 상어크기 증가
        cnt = 0 
print(ans) 