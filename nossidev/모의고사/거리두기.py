# P: 앉아있는 자리, O: 빈테이블, X: 파티션
from collections import deque
def bfs(r,c,place):
    q = deque()
    visited = [[False]*5 for _ in range(5)]
    q.append((r,c,0))
    visited[r][c] = True
    while q:
        cur_r,cur_c,cur_d = q.popleft()
        
        if cur_d >1:
            break
            
        for dr,dc in [[-1,0],[1,0],[0,1],[0,-1]]:
            nr,nc = dr+cur_r, dc+cur_c
            
            if (0<=nr<5 and 0<=nc<5 and not visited[nr][nc] and place[nr][nc] != 'X'):
                if place[nr][nc] == 'P':
                    return False
                q.append((nr,nc,cur_d+1))
                visited[nr][nc] = True
    return True
    
def check(place):
    for r in range(5):
        for c in range(5):
            if place[r][c] == 'P':
                if not bfs(r,c,place):
                    return False
    return True


def solution(places):
    result = []
    for place in places:
        if check(place):
            result.append(1)
        else:
            result.append(0)
    return result
    