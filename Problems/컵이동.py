# 컵이동문제
# def solution(cups, moves):
#     # 각 이동에서 구슬을 이동시키는 작업
#     for move in moves:
#         a, b = move[0] - 1, move[1] - 1  # 1-based index를 0-based로 변환
#         cups[b] += cups[a]  # a번 컵의 구슬을 b번 컵으로 모두 옮김

#     return cups

### 그래프 ###
def solution(cups,moves):
    n = len(cups)
    parent=[None]* (n) 

    # 부모 관계 설정 (부모: 인덱스, 자식: 값)
    for move in moves:
        a,b = move
        parent[a-1] = b-1

    # 자식관계 설정
    # 인덱스가 부모를 나타내고 각 리스트가 자식을 나타내는 구조다
    children =[[] for _ in range(n)]

    for child, p in enumerate(parent): # child: 자식(인덱스), p = 부모(값))
        if p is not None: # 부모가 없을 경우 None 값일텐데 이 값은 넣어주지 말것 (=어느 컵에도 속하지 않는 경우, 컵 하나 = 나가 부모)
            children[p].append(child)

    print(children)
    answer= [0] * n
    
    # 최상위 노드에서 최하위 노드까지 계속 내려가면서 구슬의 값을 계산해주면 됨 (= dfs)
    def dfs(node): # 최상위 노드 부터(=루트노드 = 제일 큰 컵= 부모 노드) 시작
        answer[node] = cups[node] # answer 현재 노드의 값은 cups의 현재 노드의 값이다 = 컵이 원래 갖고 있던 구슬값들로 초기화

        for child in children[node]: # 첫번째 테케라면 2,4번 노드를 돌것임 직계 자손이니까
            answer[node] += dfs(child)
        return answer[node]

    for i in range(n):
        if parent[i] is None: # 최상위 노드 찾기
            dfs(i) # 최상위 노드에서 시작
    return answer


print(solution([4, 3, 2, 1],[[3, 2], [2, 1], [4, 1]]))
print(solution([2, 3, 3, 4, 5],[[1, 2], [2, 3], [4, 5], [2, 4], [1, 3]]))