from itertools import combinations
import sys, copy
from collections import deque

sys.stdin = open('nossidev/3주차/input/연구소.txt','r')
n,m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
empty, virus = [],[]
dir = [[-1,0],[1,0],[0,-1],[0,1]]
answer =0

# 빈칸과 바이러스의 위치
for r in range(n):
  for c in range(m):
    if grid[r][c] == 0:
      empty.append((r,c))
    elif grid[r][c] == 2:
      virus.append((r,c))


# 벽 3개 세울 경우의 수
wall_cases = combinations(empty,3)

for wall in wall_cases:
  new_wall = copy.deepcopy(grid)
  for r,c in wall:
    new_wall[r][c] = 1
  
  # bfs 시작
  q = deque(virus)

  while q:
    r,c = q.popleft()
    
    for i in dir:
      nr,nc = r+i[0], c+i[1]
      if 0<=nr<n and 0<=nc<m and new_wall[nr][nc] == 0:
        q.append((nr,nc))
        new_wall[nr][nc] = 2

  # 0의 갯수 구하기 
  count = 0
  for i in range(n):
    for j in range(m):
      if new_wall[i][j] == 0:
        count +=1
  answer = max(answer,count)
print(answer)