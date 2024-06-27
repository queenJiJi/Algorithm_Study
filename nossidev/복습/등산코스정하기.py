import collections, heapq

def solution(n, paths, gates, summits):
    
    graph = collections.defaultdict(list)
    summits.sort()
    summit_set = set(summits)
    
    for u,v,w in paths:
        graph[u].append([w,v])
        graph[v].append([w,u])

    pq = []
    intense = [float('inf')]*(n+1)
    
    for gate in gates:
        heapq.heappush(pq,(0,gate))
        intense[gate] =0
        
    while pq:
        cur_intensity, cur_v = heapq.heappop(pq)
        
        if cur_v in summit_set or cur_intensity > intense[cur_v]:
            continue
            
        for intensity, next_v  in graph[cur_v]:
            next_intensity = max(cur_intensity, intensity)
            if next_intensity < intense[next_v]:
                intense[next_v] = next_intensity
                heapq.heappush(pq,(next_intensity, next_v))
                
    answer = [0,float('inf')]
    for summit in summits:
        if intense[summit] < answer[1]:
            answer = [summit, intense[summit]]
    return answer
                

print(solution(6,	[[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]],	[1, 3],	[5]))
print(solution(7,[[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]],	[1],	[2, 3, 4]))
print(solution(7,[[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]],	[3, 7],	[1, 5]))
print(solution(5,	[[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]],	[1, 2],	[5]))


