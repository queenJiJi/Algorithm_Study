# scoville 리스트를 힙(Heap)으로 바꿔줘야 한다.

# 이제 힙에서 가장 작은 값을 가진 노드(scoville[0]으로 얻을 수 있음)를 K와 비교해 줄 것이다.
# 가장 작은 값을 가진 노드가 K보다 작을 경우, 스코빌 지수가 낮은 두 노드를 pop 해서 주어진 방법으로 변환해 힙에 추가해줘야 한다.
# 이때 주의할 점은 heap에서 가장 작은 값을 뺄 때, 인덱싱 형태로 제거하게 되면 그다음 값이 최솟값이 아닐 수도 있다는 점이다!

# 이 반복 안에서 반드시 빼먹으면 안 되는 부분 하나가 -1이 반환된다는 조건이다.
# 전체 heap의 길이가 2이고, 이 두 노드끼리 음식을 섞어도 K가 되지 않는다면 더 이상
# "모든 음식의 스코빌 지수를 K 이상으로 만들 수 없다"라고 판단할 수 있으니 이때는 -1을 반환하도록 한다.
import heapq as hq


def solution(scoville, k):
    hq.heapify(scoville)
    answer = 0
    if scoville[0] >= k:
        return answer

    while scoville[0] < k:
        if len(scoville) == 1:
            return -1

        minscov1 = hq.heappop(scoville)
        minscov2 = hq.heappop(scoville)

        hq.heappush(scoville, minscov1+2*minscov2)
        answer += 1
    return answer


print(solution([1, 2, 3, 9, 10, 12], 7))


# def solution(scoville, K):
#   heapq.heapify(scoville)

#   answer = 0
#   if scoville[0] >= K:
#     return answer

#   while scoville[0] < K:
#     if len(scoville) == 1:
#       return -1

#     min_scoville = heapq.heappop(scoville)
#     min2_scoville = heapq.heappop(scoville)

#     heapq.heappush(scoville, min_scoville + min2_scoville*2)
#     answer += 1

#   return answer
