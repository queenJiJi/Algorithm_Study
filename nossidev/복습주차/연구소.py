from collections import deque
from itertools import combinations
import sys,copy
sys.stdin =open('nossidev/복습주차/input/연구소.txt','r')
# 0: 빈칸, 1: 벽, 2: 바이러스 
# 벽 3개 
# 최대 안전영역의 크기 

def solution():
#0은 빈 칸, 1은 벽, 2는 바이러스
  n,m = map(int,input().split())
  grid =[list(map(int,input().split())) for _ in range(n)]
  empty, virus = [], []
  answer= 0

  for x in range(n):
      for y in range(m):
          if grid[x][y] == 0:# 벽을 세울 수 있는 위치
              empty.append((x,y))
          elif grid[x][y] == 2:# 바이러스의 위치 
              virus.append((x,y))

  def bfs(r,c,board):  # virus들의 위치마다 BFS해서 만약 뚫려있으면 바이러스 퍼지게 하기 (0->3으로 변환)
    q= deque(virus)
    while q:
      cur_r,cur_c = q.popleft()

      for dr,dc in [[-1,0],[1,0],[0,-1],[0,1]]:
        nr,nc = cur_r+dr,cur_c+dc
        if 0<=nr<n and 0<=nc<m and new_grid[nr][nc]==0:
            new_grid[nr][nc] = 3
            q.append((nr,nc))

  for cases in combinations(empty,3):# 0들 중 3개 벽 새우는 combinations
    new_grid = copy.deepcopy(grid)# 매번이렇게 카피를 해주지 않으면 그 위에 계속 덮어쓰게 됨
  
    for r,c in cases:
        new_grid[r][c] = 1
    
    bfs(r,c,new_grid)

    count = 0
    for i in range(n):
      for j in range(m):
          if new_grid[i][j] == 0:
            count+=1
  
    answer = max(answer,count)
  return answer

print(solution())
         


