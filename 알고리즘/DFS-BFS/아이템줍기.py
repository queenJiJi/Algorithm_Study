from collections import deque

def bfs(start_x,start_y,end_x,end_y,expanded_rectangles):
    n,m = len(expanded_rectangles), len(expanded_rectangles[0])

    q = deque()
    q.append((start_x,start_y,0))
    visited = [[False]*m for _ in range(n)]
    visited[start_x][start_y]=True

    while q:
        x,y,dist = q.popleft()

        if (x,y) == (end_x,end_y):
            return dist//2
        
        for dx,dy in [[-1,0],[0,-1],[0,1],[1,0]]:
            nx,ny = dx+x, dy+y

            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and expanded_rectangles[nx][ny] == 1: # expanded_rectangles[nx][ny] == 1 = 사각형 내부가 아니라 테두리 인지
                visited[nx][ny] = True
                q.append((nx,ny,dist+1))
    return -1 # 경로가 없는 경우


def solution(rectangle, characterX, characterY, itemX, itemY):
    n = 102 
    expanded_rectangles = [[0]*n for _ in range(n)]

    # 좌표도 2배로 확장해서 사각형 표시
    for rect in rectangle:
        x1,y1,x2,y2 = map(lambda x:x*2, rect) # 좌표 확장

        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                if x1<i<x2 and y1<j<y2: # 사각형 내부
                    expanded_rectangles[i][j] = -1
                elif expanded_rectangles[i][j] != -1: # 테두리
                    expanded_rectangles[i][j] = 1

    # 좌표 2배 확장
    characterX, characterY, itemX, itemY = characterX*2, characterY*2, itemX*2, itemY*2

    return bfs(characterX, characterY, itemX, itemY,expanded_rectangles) # bfs를 사용하여 최단 거리 검색
