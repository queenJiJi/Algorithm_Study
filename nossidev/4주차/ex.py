from collections import defaultdict
from heapq import heappush, heappop

def solution(n, paths, gates, summits):
    summits.sort()
    summit_set = set(summits)

		#✅ 인풋을 본인이 쓰기 편한 구조로 바꾸기 => 무방향 그래프 만들기
    graph = defaultdict(list)
    for i, j, w in paths:
        graph[i].append((w, j))
        graph[j].append((w, i))

    hq = []
		# visited를 초기값 설정할 때, sys.maxsize등의 큰 값을 써도 되지만, 
		# 제약조건에서 주는 값의 범위보다 1큰 수를 써도 된다.
    visited = [10000001] * (n + 1)

		#✅ 모든 출입구를 우선순위큐에 삽입한다.
    for gate in gates:
        heappush(hq, (0, gate))
        visited[gate] = 0

		#✅ intensity를 기준으로 다익스트라를 진행한다.
    while hq:
        intensity, node = heappop(hq)
        if intensity > visited[node] or node in summit_set:
            continue

        for weight, next_node in graph[node]:
            next_intensity = max(weight, intensity)
            if next_intensity < visited[next_node]:
								#✅ 다익스트라 진행 중 각 노드에 도달하는 과정의 최대 intensity값을 저장한다.
                visited[next_node] = next_intensity
                heappush(hq, (next_intensity, next_node))
                

		#✅ 다익스트라 완료 후 산봉우리들을 순회하며 정답을 찾는다.
    min_intensity = [0, 10000001]
    for summit in summits:
        print(visited[summit])
        if min_intensity[1] > visited[summit]:
            min_intensity[0] = summit
            min_intensity[1] = visited[summit]

    return min_intensity

print(solution(6,[[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1,3],[5]))
print(solution(7,[[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [1],[2,3,4]))
print(solution(7,[[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1]] ,[3,7], [1,5]))
print(solution(5,	[[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]],	[1, 2],	[5]))