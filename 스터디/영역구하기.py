import sys
from collections import deque
sys.stdin= open('스터디/영역.txt','r')
answer = []
count_result = 0
M,N,K = map(int,input().split())
board = [[0]*N for _ in range(M)]

def bfs(x,y):
  q= deque([(x,y)])
  board[x][y]= 1 # 방문 처리
  cnt = 1
  while q:
    x,y = q.popleft()
    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
      nx,ny = x+dx, y+dy
      if (0<=nx<M )and (0<=ny<N) and (board[nx][ny] == 0):
        board[nx][ny] = 1
        q.append((nx,ny))
        cnt+=1
  return cnt

def dfs(x,y,cnt):
  board[x][y] =1 # 방문처리
  for dx,dy in [[-1,0],[0,1],[1,0],[0,-1]]:
    nx,ny = x+dx, y+dy
    if (0<=nx<M) and (0<=ny<N) and (board[nx][ny]==0):
      cnt = dfs(nx,ny,cnt+1)
  return cnt

for _ in range(K):
  x1,y1, x2,y2 = map(int, input().split())
  for r in range(y1,y2):
    for c in range(x1,x2):
      board[r][c] = 1

for i in range(M):
  for j in range(N):
    if board[i][j] == 0:
      cnt= 1
      # answer.append(bfs(i,j))
      answer.append(dfs(i,j,cnt))

answer.sort()
print(len(answer))
print(*answer)

