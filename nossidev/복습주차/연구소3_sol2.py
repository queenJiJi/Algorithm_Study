from itertools import combinations
from collections import deque
import sys
sys.stdin = open('nossidev/복습주차/input/연구소3.txt','r')

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]

# 바이러스와 빈칸의 위치
def locate():
    virus = []
    num_blank = 0
    for r in range(n):
        for c in range(n):
            if lab[r][c] == 2:
                virus.append((r, c))
            elif lab[r][c] == 0:
                num_blank+=1
    return num_blank, virus

def bfs(q,visited,num_blank):
    max_path = 0
    while q:
        cur_r, cur_c, cur_d = q.popleft()
        visited.add((cur_r,cur_c))

        for dr, dc in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
            nr, nc = cur_r + dr, cur_c + dc

            if 0 <= nr < n and 0 <= nc < n and (nr,nc) not in visited:
                if  lab[nr][nc]==0:
                    q.append((nr, nc, cur_d + 1))
                    visited.add((nr,nc))
                    max_path = max(max_path, cur_d + 1)
                    num_blank-=1

                    if num_blank == 0:
                        return max_path
                    
                elif lab[nr][nc] == 2:
                    q.append((nr, nc, cur_d + 1))
                    visited.add((nr,nc))

    return -1

def solution():
    result = float("inf")
    num_blank,virus= locate()
    for comb in combinations(virus, m):
        q = deque()
        visited = set()

        for r, c in comb:
            q.append((r, c, 0))

        if num_blank == 0: 
            result = 0
            break
        
        ret = bfs(q,visited,num_blank)
    
        if ret != -1:
            result = min(result, ret)

    if result != float("inf"):
        print(result)
    else:
        print(-1)

solution()