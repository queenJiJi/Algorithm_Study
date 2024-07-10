def solution(cook_times, order, k):
    from collections import defaultdict, deque
    answer=[0,0]
    graph = defaultdict(list)
    bfs_graph = defaultdict(list)
    indegree = [0] * len(cook_times)
    
    for u,v in order:
        graph[u].append(v)
        indegree[v-1] += 1
        bfs_graph[v].append(u)   
    
    visited=set()
    bfs_q = deque([k])
    
    while bfs_q:
        cur_node = bfs_q.popleft() 

        for next_node in bfs_graph[cur_node]:
            if next_node not in visited:
                visited.add(next_node)   
                answer[0]+=1
                bfs_q.append(next_node)

    q=deque()
    time=cook_times[:]
    for node in range(len(indegree)):
        if indegree[node-1] == 0:
            q.append(node)

    while q:
        cur_v = q.popleft()

        for next_v in graph[cur_v]:
            indegree[next_v-1] -= 1
            if indegree[next_v-1] == 0:
                q.append(next_v)
            time[next_v-1] = max(cook_times[next_v-1]+time[cur_v-1], time[next_v-1])
    answer[1] = time[k-1]
    return answer    


print(solution([5, 30, 15, 30, 35, 20, 4],[[2,4], [2,5], [3,4], [3,5], [1,6], [4,6], [5,6], [6,7]],6))
print(solution([5, 30, 15, 30, 35, 20, 4, 50, 40],[[2,4], [2,5], [3,4], [3,5], [1,6], [4,6], [5,6], [6,7], [8,9]],9))
print(solution([5, 3, 2],[[1,2], [2,3], [1,3]],3))