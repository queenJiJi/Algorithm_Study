from collections import deque,defaultdict

def solution(n,passenger,train):
    graph = defaultdict(list)

    for u,v in train:
        graph[u].append(v)    
        graph[v].append(u)    
    
    answer= [0,0]
    q= deque()
    q.append((1,passenger[0]))

    while q:
        cur_node, p = q.popleft()  
        # 더해가면서 인원수가 더 많거나 인원수은 같은데 노드값이 더 크다면 answer갱신
        if p>answer[1] or ( p==answer[1] and cur_node>answer[0] ):
            answer = [cur_node,p]
        for next_node in list(graph[cur_node]): # list로 해줘야 원본에 손실안감
            next_p = p+passenger[next_node-1]
            q.append((next_node,next_p))
            graph[cur_node].remove(next_node) # 방문 표시
            graph[next_node].remove(cur_node) # 방문 표시

    return answer


print(solution(6,[1,1,1,1,1,1],	[[1,2],[1,3],[1,4],[3,5],[3,6]]))
print(solution(4,[2,1,2,2],[[1,2],[1,3],[2,4]]))    
print(solution(5,[1,1,2,3,4],[[1,2],[1,3],[1,4],[1,5]]))

