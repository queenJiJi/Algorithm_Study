from collections import deque


def solution(priorities, location):
    count = 0
    # arr = sorted(priorities, reverse=True)
    # arr = list((x, i) for i, x in enumerate(
    #     sorted(priorities), reverse=True, start=1))
    # arr.sort(reverse=True)
    arr = [(i, x) for i, x in enumerate(priorities)]
    print(arr)
    # q = deque(pririties)
    while 1:
        v = arr.pop(0)  # 큐에서 순서대로 pop
        if any(v[1] < i[1] for i in arr):
            arr.append(v)
        else:
            count += 1
            if v == location:
                return count


print(solution([2, 1, 3, 2],	2))
print(solution([1, 1, 9, 1, 1, 1],	0))


def solution(priorities, location):
    queue = [(i, p) for i, p in enumerate(priorities)]  # 인덱스와 값 같이 저장
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):  # 큰 값이 하나라도 있으면
            queue.append(cur)  # 다시 추가
        else:  # 큰 값이 없으면
            answer += 1   # 카운트 증가 (빼냄)
            if cur[0] == location:  # 이게 타겟 값이면
                return answer  # 정답 리턴
