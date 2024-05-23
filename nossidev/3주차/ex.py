from collections import deque

def bfs(r,c,dist,place):
  visited = [[False]* 5 for _ in range(5)]
  q = deque()
  q.append((r,c,dist))
  visited[r][c] = True

  while q: 
    cur_r,cur_c,cur_dist = q.popleft()  
    
    # print('hi',cur_dist)
    if cur_dist >2: # 만약 맨하튼 거리가 2보다 크다면 멈추기 
      continue

    if cur_dist!=0 and place[cur_r][cur_c] == 'P':
      return False

    for dr,dc in [[-1,0],[1,0],[0,1],[0,-1]]:
      next_r,next_c= cur_r+dr, cur_c+dc

      if 0>next_r or next_r>=5 or 0>next_c or next_c>=5:
        continue

      if visited[next_r][next_c]:
        continue

      if place[next_r][next_c] =='X':
        continue
        
      q.append((next_r,next_c,cur_dist+1)) # 다음 위치와 맨해튼 거리를 큐에 넣기
      visited[next_r][next_c]= True
  return True # 다 돌고도 return 0 에 걸리지 않았다면 거리두기 성공(1)반환

def check(place):
  for r in range(5):
    for c in range(5):
      if place[r][c] == 'P':
        if not bfs(r,c,0,place):
          return False
  return True

def solution(places):
  answer = []
  for place in places:
    if check(place):
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