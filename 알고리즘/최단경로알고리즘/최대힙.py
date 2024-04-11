# 기본적으로 파이썬은 최소힙을 제공하기때문에 '최대힙'을 구현하기 위해선 조작이 필요
# 넣을때와 뺄때 원소의 부호를 원래 원소의 부호와 반대로해서 넣고,빼면 됨
import heapq

# 내림차순 힙 정렬(Heap Sort)


def heapsort(iterable):
    h = []
    result = []

    # 모든 원소를 차례대로 힙에 삽입
    for val in iterable:
        heapq.heappush(h, -val)

    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result


result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)
