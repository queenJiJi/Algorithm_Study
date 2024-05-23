from collections import  deque

def bfs(r,c,place):
    visited=[[False]*5 for _ in range(5)]
    q=deque()
    q.append((r,c,1))
    visited[r][c] = True
    
    while q: 
        cur_r,cur_c,cur_dist = q.popleft()
        
        if cur_dist > 2: # 검사하는 거리가 2 이상이면 멈추기
            break
            
        for dr,dc in [[-1,0],[1,0],[0,-1],[0,1]]: # 멘해튼 거리를 보는 것이니 대각선은 미포함
            nr,nc,nd = cur_r+dr,cur_c+dc,cur_dist+1
            
            if(0<=nr<5 and 0<=nc<5 and not visited[nr][nc] and place[nr][nc]!='X'):
                if place[nr][nc] == 'P':
                    return False # 거리가 2 이하면서 bfs를 통해 주변을 살폈을 때 P를 만난 것이니 거리두기 실패
                q.append((nr,nc,nd))
                visited[nr][nc] = True
    return True # 다 체크해봤는데도 False에 걸리는 것이 없다는 것은 거리두기 성공
    


def check(place):
    for r in range(5):
        for c in range(5):
            if place[r][c] == 'P':
                if not bfs(r,c,place):#거리두기 실패를 만났인 경우 더 이상 할 것 없이
                    return False # 바로 False리턴
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