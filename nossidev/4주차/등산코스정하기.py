import heapq, collections

'''
인풋을 본인이 쓰기 편한 구조로 바꾸기 => 무방향 그래프 만들기
    - 모든 출입구를 우선순위큐에 삽입한다.
    - intensity를 기준으로 다익스트라를 진행한다.
    - 다익스트라 진행 중 각 노드에 도달하는 과정의 최대 intensity값을 저장한다.
    - 다익스트라 완료 후 산봉우리들을 순회하며 정답을 찾는다.
'''

# def solution(n,paths,gates,summits):
#   graph = collections.defaultdict(list)

#   for i,j,w in paths:
#     graph[i].append((w,j))
#     graph[j].append((w,i)) # 무방향 그래프이기 때문에 양방향으로 연결해줘야함

#   summits.sort() # 결과값들 중에서 가장 작은 봉우리 수를 return해야하기 때문에 
#   summit_set = set(summits)

#   intense = [float('inf')] * (n+1)

#   pq = []
  
#   for gate in gates:
#     heapq.heappush(pq,(0,gate))

#   while pq:
#     cur_intense, cur_node = heapq.heappop(pq)

#     # 매 순간 최소인 intensity를 골라야하므로, 노드의 저장된 intensity보다 현재 intensity가 더 클 경우 다른 경로를 찾음, 현재 노드가 봉우리라고 해도 넘어감 
#     if cur_intense > intense[cur_node] or cur_node in summit_set: 
#       continue

#     for intensity, next_node in graph[cur_node]:
#       next_intensity = max(intensity, cur_intense) #최소 intensity들 중에서 최대 intensity저장 
#       if next_intensity < intense[next_node]:
#         intense[next_node] = next_intensity
#         heapq.heappush(pq,(next_intensity, next_node))
#   print(intense)
#   # 봉우리들 중 정답찾기
#   answer = [0,float('inf')] # [산봉우리의번호, intensity의 최소값]
#   for summit in summits:
#     if answer[1] > intense[summit]:
#       answer = [summit, intense[summit]]
#   return answer


# print(solution(6,[[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1,3],[5]))
# print(solution(7,[[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [1],[2,3,4]))
# print(solution(7,[[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1]] ,[3,7], [1,5]))
# print(solution(5,	[[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]],	[1, 2],	[5]))


import heapq
import collections

'''
인풋을 본인이 쓰기 편한 구조로 바꾸기 => 무방향 그래프 만들기
    - 모든 출입구를 우선순위큐에 삽입한다.
    - intensity를 기준으로 다익스트라를 진행한다.
    - 다익스트라 진행 중 각 노드에 도달하는 과정의 최대 intensity값을 저장한다.
    - 다익스트라 완료 후 산봉우리들을 순회하며 정답을 찾는다.
'''

def solution(n, paths, gates, summits):
    graph = collections.defaultdict(list)

    for i, j, w in paths:
        graph[i].append((w, j))
        graph[j].append((w, i))  # 무방향 그래프이기 때문에 양방향으로 연결

    summits.sort()  # 결과값들 중에서 가장 작은 봉우리 수를 반환하기 위해 정렬
    summit_set = set(summits)

    intense = {}  # 각 노드에 도달하는 경로의 최대 intensity 값을 저장할 딕셔너리

    pq = []
    
    for gate in gates:
        heapq.heappush(pq, (0, gate))
       
    while pq:
        cur_intense, cur_node = heapq.heappop(pq)

        # if cur_node in summit_set:  # 현재 노드가 산봉우리이면 넘어감
        #     continue

        # if cur_node in intense and cur_intense > intense[cur_node]:
        #     continue  # 노드의 저장된 intensity보다 현재 intensity가 더 크다면 다른 경로를 탐색
        
        if cur_node not in intense:
            intense[cur_node] = cur_intense

            if cur_node in summit_set:  # 현재 노드가 산봉우리이면 넘어감
              continue


            for intensity, next_node in graph[cur_node]:
                next_intensity = max(intensity, cur_intense)  # 최소 intensity들 중에서 최대 intensity 저장
                # if next_node not in intense or next_intensity < intense[next_node]:
                #     intense[next_node] = next_intensity
                heapq.heappush(pq, (next_intensity, next_node))

    # print(intense)

    # 봉우리들 중 정답 찾기
    answer = [0, float('inf')]  # [산봉우리의 번호, intensity의 최소값]
    for summit in summits:
        if summit in intense and answer[1] > intense[summit]:
            answer = [summit, intense[summit]]
    return answer

# 테스트 케이스
print(solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]))
print(solution(7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2, 3, 4]))
print(solution(7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1],[6,7,1]], [3, 7], [1, 5]))
print(solution(5, [[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]], [1, 2], [5]))
