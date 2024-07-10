from collections import deque, defaultdict

def solution(cook_times, order, k ):
    answer = [0,0]
    bfs_graph = defaultdict(list) # bfs를 위한 그래프
    graph = defaultdict(list) # 위상정렬을 위한 그래프
    indegree= [0] * len(cook_times)
        ## bfs가 역순 그래프인 이유: 정확힌 위상정렬그래프가 역순임, 들어오는 방향을 기준으로 그래프를 만드는 것이니까, 하지만
        ## bfs는 그냥 연결된 그래프니까 진입을 기준으로 만드는 그래프와 반대로 연결된 그래프여야하니까 역순이라고치는 것임
    
    # bfs를 위한 그래프(원래의 역순)와 위상정렬을 위한 그래프 생성 
    for u,v in order:
        graph[u].append(v)
        indegree[v-1]+=1
        bfs_graph[v].append(u)
    

    # bfs - k단계까지 도달하기 위한 단계 수 = k 노드와 연결된 노드의 갯수 구하기
    visited=set()
    bfs_q = deque([k]) #k와 연결된 노드의 갯수를 세야함
    while bfs_q:
        cur_node = bfs_q.popleft()

        for next_v in bfs_graph[cur_node]:
            if next_v not in visited:
                visited.add(next_v)
                answer[0]+=1
                bfs_q.append(next_v)

    
    # 위상정렬 - k단계까지의 최소소요시간 구하기 
    q= deque()
    time = cook_times[:]
    # 위상정렬 q 초기값 세팅
    for node in range(len(indegree)):
        if indegree[node-1] == 0: # 진입차수가 0인 것부터 노드를 돌아야해서 그 값들부터 q에 넣어주기
            q.append(node)
    
    while q:
        cur_v = q.popleft()
        for next_v in  graph[cur_v]:
            indegree[next_v-1] -=1
            if indegree[next_v-1] == 0:
                q.append(next_v)
            time[next_v-1] = max(cook_times[next_v-1]+ time[cur_v-1], time[next_v-1])
    answer[1] = time[k-1]
    return answer


print(solution([5, 30, 15, 30, 35, 20, 4],[[2,4], [2,5], [3,4], [3,5], [1,6], [4,6], [5,6], [6,7]],6))
print(solution([5, 30, 15, 30, 35, 20, 4, 50, 40],[[2,4], [2,5], [3,4], [3,5], [1,6], [4,6], [5,6], [6,7], [8,9]],9))
print(solution([5, 3, 2],[[1,2], [2,3], [1,3]],3))

