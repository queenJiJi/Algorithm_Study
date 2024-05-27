import sys, collections

sys.stdin = open("nossidev/3주차/input/스타트택시.txt",'r')

n,m,fuel = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
tr,tc = map(int,input().split())
tr-=1
tc-=1
answer = 0

# 승객의 출발지와 도착지를 해시테이블에 저장한다.
passengers = {}
for i in range(m):
  pr,pc,pdr,pdc = list(map(int,input().split()))
  passengers[(pr-1,pc-1)] = (pdr-1,pdc-1)
 #  택시의 현재 위치로부터 가장 가까운 승객의 위치와 거리 반환 (BFS)
def pickup(tr,tc):
  cand = []
  min_dist = 1000000
  q= collections.deque()
  visited=set([(tr,tc)])
  q.append((tr,tc,0))

  while q: 
    cur_r,cur_c,cur_d = q.popleft()

    # base case: 스타트에서 현재 지점까지의 거리가 가장 가까운 승객까지의 거리보다 길다면더 이상 순회를 돌 필요가 없음. bfs니까 어차피 계속 돌아봤자 더 멀어질 뿐
    if cur_d > min_dist:
      break
    
    if (cur_r,cur_c) in passengers:
      cand.append((cur_r,cur_c))
      min_dist = cur_d

    for dr,dc in [[-1,0],[1,0],[0,-1],[0,1]]:
      nr,nc,nd = cur_r+dr,cur_c+dc,cur_d+1
      if (nr,nc) in visited:
        continue
      if 0<=nr<n and 0<=nc<n and board[nr][nc]!=1:
        q.append((nr,nc,nd))
        visited.add((nr,nc))   
  return cand,min_dist  # 스타트지점으로부터 가장 가까운 승객의 좌표와 거리를 리턴


# 손님을 태우고 도착지까지 가는 bfs(도착지까지 가는데 얼마나 비용이드는지 계산하기 위함)
def go_dest(tr,tc):
  pdr,pdc = passengers[(tr,tc)]
  del passengers[(tr,tc)]   # 데려다 준 손님은 삭제(dictionary의 key를 삭제하는 키워드: del), otherwise, 이미 목적지에 도착한 승객을 또 픽업할수도있고 무한루프
  q= collections.deque()
  visited=set((tr,tc))
  q.append((tr,tc,0))

  while q:
    cur_r,cur_c,cur_d = q.popleft()
    # base case 만약 현재 위치가 목적지위치(도착지)라면 현재 위치와 이동거리 반환
    if (cur_r,cur_c) ==(pdr,pdc):
      return cur_r,cur_c,cur_d
    
    for dr,dc in [[-1,0],[1,0],[0,-1],[0,1]]:
      nr,nc,nd = cur_r+dr,cur_c+dc,cur_d+1
      if (nr,nc) in visited:
        continue
      if 0<=nr<n and 0<=nc<n and board[nr][nc]!=1:
        q.append((nr,nc,nd))
        visited.add((nr,nc))   
  # 여기까지 왔다면 목적지에 도달하지 못했다는 의미(택시가 벽에 막혀서 이동할수 없었음) 따라서 10^7이라는 큰수를 반환하여 연료를 모두 고갈시킴
  return pdr,pdc,10000000


# 남아있는 승객이 있다면 반복문을 수행한다.
while len(passengers)!=0 and fuel>0:
	# BFS 알고리즘으로 현재 택시 위치로부터 승객까지의 최단거리를 계산한다.
  cand, used_fuel = pickup(tr,tc)
  
  if fuel>used_fuel or len(cand)!=0: #만약 연료가 다 떨어졌거나 어떠한 승객에도 도달할수없다면(벽에 의해)
    tr,tc = sorted(cand)[0] # 최단거리를 기준으로 가장 높은 우선순위의 승객 위치로 택시를 이동시킨다.
    fuel -= used_fuel# 손님한테까지 가는데 드는 연료 차감
  else:
    answer = -1
    break
	# 연료가 충분하다면 BFS 알고리즘을 통해 승객을 도착지까지 이동시키고 연료를 보충받는다.
  pdr,pdc,used_fuel = go_dest(tr,tc)
# 이렇게 다녀왔는데 연료가 중간에 고갈되었다면 
  if fuel<used_fuel:
    answer= -1
    break # -1 반환
  fuel+=used_fuel  # 연료가 고갈되지 않았다면 사용한 값을 빼주고 사용한 만큼 *2 해줌 = 즉, + 사용한 만큼 채우기
  tr,tc = pdr,pdc# 손님을 내려준 곳(=손님의목적지)가 다시 택시의 출발점이 됨
# 이동 성공 여부에 따라 출력값을 결정한다.
if answer == -1:
  print(-1) # 승객 이동시키기에 실패한다면 -1를 출력한다.
else:
  print(fuel) # 모든 승객 이동시키기에 성공한다면 남은 연료를 출력한다.
