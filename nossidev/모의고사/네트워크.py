# BFS
from collections import deque

def solution(n,computers):
    answer = 0
    visited = [False] * n
    
    def bfs(start_v):
        q=deque()
        q.append(start_v)
        while q:
            cur_v = q.popleft()
            for next_v in range(n):
                if not visited[next_v] and computers[cur_v][next_v] == 1:
                    visited[next_v] = True
                    q.append(next_v)
    
    
    # 각 노드 마다 실행
    for cur_node in range(n):
        if not visited[cur_node]:
            bfs(cur_node)
            answer+=1
    return answer




# DFS
def solution(n,computers):
    answer = 0
    visited = [False] * n
    
    def dfs(cur_v):
        visited[cur_v] = True
        for next_v in range(n):
            if not visited[next_v] and computers[cur_v][next_v] == 1:
                dfs(next_v)
    
    
    # 각 노드 마다 실행
    for cur_node in range(n):
        if not visited[cur_node]:
            dfs(cur_node)
            answer+=1
    return answer