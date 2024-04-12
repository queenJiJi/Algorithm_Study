# 기본적으로 파이썬은 최소힙을 제공
# 따라서 그냥 iterable한 객체(리스트)를 그냥 힙에 넣었다 꺼내기만 해도 오름차순 정렬이 가능
import heapq

# 힙 자료구조의 특징:
# 데이터를 꺼낼때 우선순위가 높은 데이터(큰 수)부터 꺼낸다는 특징이 있음
# 이러한 자료구조의 특성을 활용해서 정렬을 수행할 수 있음
# 그런데, 파이썬의 힙라이브러리는 기본적으로 Min Heap(최소힙)이 디폴트라서
# 우선순위가 낮은 데이터(작은 수)부터 꺼낸다는 특징이 있어서 오름차순 정렬이 가능

# 오름차순 힙 정렬(Heap Sort)


def heapsort(iterable):
    h = []
    result = []

    # 모든 원소를 차례대로 힙에 삽입
    for val in iterable:
        heapq.heappush(h, val)

    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result


result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)  # [0,1,2,3,4,5,6,7,8,9]
