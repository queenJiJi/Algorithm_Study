import itertools, sys,copy,collections

sys.stdin = open('nossidev/3주차/input/연구소3.txt','r')
n,m = map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(n)]
virus =[]
dir = [[-1,0],[1,0],[0,-1],[0,1]]
path = 0
answer=[]

def contains_no_zero(grid):
    for row in grid:
        if 0 in row:
            return False
    return True

# 1. 바이러스의 위치를 저장
for r in range(n):
  for c in range(n):
    if grid[r][c] == 2:
      virus.append((r,c))
      
# 2. 바이러스의 위치들 중 m개의 활성 바이러스 가능한 경우의 수들을 구함
for cases in itertools.combinations(virus,m):
  # new_grid = copy.deepcopy(grid)
  new_grid = [grid[i][:] for i in range(n)]
  # 2-1. 그 경우의 수에 해당하는 값을 바이러스로 변환 
  for r,c in cases:
    new_grid[r][c] = 'v' # 바이러스로 변환
  # 2-2. 나머지는 비활성 바이러스로 변환 
  for r in range(n):
    for c in range(n):
      if new_grid[r][c] == 2:
        new_grid[r][c] = '*' # 비활성 바이러스
      elif new_grid[r][c] == 1:
        new_grid[r][c] = '-' # 벽

  
  # 3. 바이러스 위치를 시작으로 bfs를 돌려서 그 주변 숫자들을 얼마나 시간이 걸리는지 칸을 채워주기 
  # print(cases)
  q = collections.deque()
  for r,c in cases:
    q.append((r,c,0))

  max_np = 0
  while q:
    cur_r,cur_c,cur_path =q.popleft()
    # print(cur_r,cur_c,cur_path)
    for dr in dir:
      nr,nc,np = cur_r+dr[0],cur_c+dr[1],cur_path+1
      if 0<=nr<n and 0<=nc<n:
        if new_grid[nr][nc]==0:
          new_grid[nr][nc] = np
          max_np = max(max_np,np)
          q.append((nr,nc,np))
        elif new_grid[nr][nc]=='*': # 인접지점이 비활성 바이러스면 전파시간 갱신하지 않고 넘어가기
          new_grid[nr][nc] = np
          q.append((nr,nc,np))
          # continue
  # for i in new_grid:
  #   print(*i)
  # print()

  if contains_no_zero(new_grid):
    answer.append(max_np)  # 모든 칸을 채웠으면 그 중 가장 큰 수를 answer에 apppend 
if not answer:
  print(-1) # 칸을 모두 채우지 못햇으면 -1을 answer에 append
else:
  print(min(answer)) # answer 중 가장 작은 값 반환
  


