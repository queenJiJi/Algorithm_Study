import sys, collections

sys.stdin = open('nossidev/3주차/input/구슬탈출.txt','r')

n,m = map(int,input().split())
board= [input().rstrip() for _ in range(n)]
visited= set()
answer = 0

# 빨간 구슬과 파란 구슬의 위치 저장
for r in range(n):
  for c in range(m):
    if board[r][c] == 'R':
      rr,rc = r,c
    elif board[r][c] == 'B':
      br,bc = r,c
q = collections.deque()
q.append([rr,rc,br,bc,1])
visited.add((rr,rc,br,bc))

def move(r,c,dr,dc):
  count = 0

  while board[r+dr][c+dc] != '#' and board[r][c] != 'O':
    r+=dr
    c+=dc
    count+=1
  return r,c, count

def bfs():
  global answer

  while q:
    cur_rr,cur_rc,cur_br,cur_bc,level = q.popleft()
 
    if level > 10:
      break

    for dr,dc in [[-1,0],[1,0],[0,-1],[0,1]]:
      next_rr,next_rc,r_count = move(cur_rr,cur_rc,dr,dc)
      next_br,next_bc,b_count = move(cur_br,cur_bc,dr,dc)

      if (next_rr,next_rc,next_br,next_bc) in visited:
        continue

      if board[next_br][next_bc] =='O': # 다음순서가 파란 구슬이 구멍에 먼저 들어갔을 때 다른 방향으로 기울여야함
        continue

      if board[next_rr][next_rc] == 'O': # 다음 순서가 빨간 구슬이 구멍에 들어가면
        answer = 1
        return answer

      if (next_br==next_rr) and (next_bc==next_rc): # 두 구슬이 충돌(한칸에 들어오려고할때)
        if b_count>r_count: # 더 많이 간 구슬을 하나 뒤로 움직여줌
          next_br -= dr
          next_bc -= dc
        else:
          next_rr -= dr
          next_rc -= dc

      q.append([next_rr,next_rc,next_br,next_bc, level+1])
      visited.add((next_rr,next_rc,next_br,next_bc))
  return answer

print(bfs())