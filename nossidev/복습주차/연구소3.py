# 0: 빈칸, 1: 벽, 2: 바이러스
# M 개를 활성상태로 변경 
# 벽: -, 비활성바이러스: *, 활성바이러스:0, 숫자: 바이러스가 퍼지는 시간

# 바이러스의 위치에 따라 각 경우의 수 별로 모두 체크 -> 최소 시간 출력-> 각 시간을 넣어줄 [] 필요
# 바이러스를 어떻게 놓아도 모든 빈칸에 바이러스를 퍼뜨릴 수 없는 경우엔 -1출력
from itertools import combinations
from collections import deque
import sys,copy
sys.stdin = open('nossidev/복습주차/input/연구소3.txt','r')

n,m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]
# visit = [[False]* n for _ in range(n)] # 왜 여기선 visit이 필요하지 않을까?
virus =[]
result = float('inf')

# 바이러스와 벽의 위치
for r in range(n):
  for c in range(n):
    if lab[r][c] == 2:
      lab[r][c] = '*'
      virus.append((r,c))
    elif lab[r][c] == 1:
      lab[r][c] = '-'
   
# def bfs(r,c,new_lab):
def bfs(q, new_lab):
  
  max_path = 0
  # visit[r][c] = True
  
  while q:
    cur_r,cur_c,cur_d = q.popleft()
    
    for dr,dc in [[-1,0],[1,0],[0,1],[0,-1]]:
      nr,nc = cur_r+dr, cur_c+dc
      # if 0<=nr<n and 0<=nc<n and new_lab[nr][nc]!='-' and not visit[nr][nc]:
      if 0<=nr<n and 0<=nc<n:
        if new_lab[nr][nc]==0 :
          q.append((nr,nc,cur_d+1))
          new_lab[nr][nc] = cur_d+1
          max_path = max(max_path,cur_d+1)
        elif new_lab[nr][nc] == '*':
          q.append((nr,nc,cur_d+1))
          new_lab[nr][nc] = cur_d+1
  for row in new_lab:
    if 0 in row:
      return -1 # 빈칸이 남아있으면 -1 반환

  return max_path
        # visit[nr][nc] = True
  

for comb in combinations(virus,m):
  print(comb)
  new_lab = copy.deepcopy(lab)
  q = deque()
  for r,c in comb: 
    new_lab[r][c] == 'V'
    q.append((r,c,0))
  ret = bfs(q,new_lab)
  if ret != -1:
    result = min(result,ret)
  
  #   result = bfs(r,c,new_lab)
if result != float('inf'):
  print(result)
else:
  print(-1)  
