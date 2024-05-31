from collections import deque
from itertools import combinations
import sys,copy
sys.stdin =open('nossidev/복습주차/input/연구소.txt','r')
# 0: 빈칸, 1: 벽, 2: 바이러스 
# 벽 3개 
# 최대 안전영역의 크기 
n,m = map(int,input().split())
grid =[list(map(int,input().split())) for _ in range(n)]

def locate():
    blank_num, virus, wall = 0, [], []

    for x in range(n):
        for y in range(m):
            if grid[x][y] == 0:# 벽을 세울 수 있는 위치
                wall.append((x,y))
                blank_num+=1 # 0의 갯수 count
            elif grid[x][y] == 2:# 바이러스의 위치 
                virus.append((x,y))
    return blank_num,virus,wall

def bfs(q,visited,blank_num):  # virus들의 위치마다 BFS해서 만약 뚫려있으면 바이러스 퍼지게 하기 
    
    while q:
        cur_r,cur_c = q.popleft()
        visited.add((cur_r,cur_c))

        for dr,dc in [[-1,0],[1,0],[0,-1],[0,1]]:
            nr,nc = cur_r+dr,cur_c+dc
            if 0<=nr<n and 0<=nc<m and (nr,nc) not in visited and grid[nr][nc]==0:
                q.append((nr,nc))
                visited.add((nr,nc))
                blank_num -= 1

    return blank_num


def solution():
#0은 빈 칸, 1은 벽, 2는 바이러스
  answer= 0
  blank_num, virus, wall = locate()

  for cases in combinations(wall,3):# 0들 중 3개 벽 새우는 combinations
    # new_grid = copy.deepcopy(grid)# 매번이렇게 카피를 해주지 않으면 그 위에 계속 덮어쓰게 됨
    q = deque()
    visited = set()

    for r,c in cases: # 벽 세우기
        grid[r][c] = 1
        # q.append((r,c))
    
    for r,c in virus:# 바이러스 위치들 append
        q.append((r,c))

    ret = bfs(q,visited,blank_num-3) # 위에서 벽 3개를 세웠으니까 0의 갯수 3개 줄이고 보내기

    answer = max(answer,ret)

    for r,c in cases: # 벽 다시 허물기 -> deepcopy를 안해주는 대신 벽을 다시 0으로 돌려놔야 새로운 case를 돌때 새grid에서 돌것
        grid[r][c] = 0 

  return answer

print(solution())
         


