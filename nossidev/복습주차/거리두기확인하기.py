# 맨하튼 거리 2이하로 앉지말기 - 상하좌우, 2까지 bfs
# 빈테이블: O, 파티션: X, 응시자가 앉는 자리: P 
# 거리두기 지키면 1, 안지키면 0 return
from collections import deque
def solution(places):
  answer = []

  def bfs(r,c,p):
    q= deque()
    visited= [[False]*5 for _ in range(5)]
    q.append((r,c,1))
    visited[r][c] = True 

    while q:
      cur_r,cur_c,cur_dist = q.popleft()
      
      if cur_dist >2:
        break

      for dr,dc in [[-1,0],[1,0],[0,-1],[0,1]]:
        nr,nc,nd = cur_r+dr,cur_c+dc, cur_dist+1
        if (0<=nr<5 and 0<=nc<5 and not visited[nr][nc] and p[nr][nc] != 'X' ):
          if p[nr][nc] == 'P':
            return False
          q.append((nr,nc,nd))
          visited[nr][nc] = True
    return True
  
  def check(p):
    for r in range(5):
      for c in range(5):
        # print((r,c))
        if p[r][c] == 'P':
          if not bfs(r,c,p):
            return False
    return True
        
  for p in places:
    # for p in place:
      if check(p):
        answer.append(1)
      else:
        answer.append(0)
  return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
                ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
                ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
                ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
print(solution([["POOOO", "XPOOO", "OOOOO", "OOOOO", "OOOOO"], 
                  ["OOOOO", "OOOOO", "OOOOO", "OOOOO", "OOOOO"], 
                  ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], 
                  ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
                  ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))







