import sys, collections

sys.stdin = open("nossidev/3주차/input/스타트택시.txt",'r')


n,m,fuel = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
tr,tc = map(int,input().split())

# 승객의 출발지와 도착지를 해시테이블에 저장
passengers = {}
for i in range(m):
  pr,pc, pdr,pdc = list(map(int,input().split()))
  passengers[(pr-1,pc-1)] = (pdr-1,pdc-1)

answer = 0


def pickup(tr,tc):
  q = collections.deque([tr,tc,0])
  visited=set([(tr,tc)])
  candidates = []
  min_dist = 10000000

  while q:
    cur_r,cur_c,cur_d = q.popleft()
    if cur_d > min_dist :
      break
    if (cur_r,cur_c) in passengers:
      candidate.append((cur_r,cur_c))
      min_dist = cur_d
    for dr,dc in [[-1,0],[1,0],[0,-1],[0,1]]:
      next_r,next_c,next_d = cur_r+dr, cur_c+dc, cur_d+1
      if (next_r,next_c) in visited:
        continue
      if 0<=next_r<n and 0<=next_c<n and board[next_r][next_c] !=1:
        q.append([next_r,next_c,next_d])
        visited.add((next_r,next_c))
  return candidate,min_dist


def go_dest(tr,tc):
  pdr,pdc = passengers[(tr,tc)]



# 남아 있는 승객이 있다면 반복문 수행
while fuel>0 and len(passengers) != 0:
  # 현재 택시위치로 부터 승객까지의 최단 거리 계산 (bfs사용)
  candidate, used_fuel = pickup(tr,tc)
  if used_fuel > fuel or len(candidate) == 0: 
    answer = -1
    break
  # 최단거리를 기준으로 가장 높은 우선순위의 승객 위치로 택시 이동
  tr,tc = sorted(candidate)[0]
  # 연료가 충분하다면 승객을 도착지까지 이동시키고 연료를 보충받음 (bfs사용)
  fuel -= used_fuel
  pdr,pdc,used_fuel = go_dest(tr,tc)
  if used_fuel > fuel:
    answer = -1
    break
  fuel += used_fuel
  tr,tc = pdr,pdc

if answer == -1:
  print(-1)
else:
  print(fuel)