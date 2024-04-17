# https://www.youtube.com/watch?v=zpz8SMzwiHM
from collections import deque


def solution(food_times, k):
    # q = deque(food_times)
    # answer = 0
    # while k > 0:
    #     for i in range(sum(food_times)):
    #         if k == 1:
    #             # answer = food_times[i % len(food_times)]
    #             answer = food_times.index(food_times[i % len(food_times)])
    #             return answer
    #         x = q.popleft()
    #         if not q:
    #             return -1
    #         if x == 0:
    #             continue
    #         q.append(x-1)
    #         k -= 1

    while k > -1:
        for i in range(sum(food_times)):
            if k == 0:
                return i % len(food_times)+1
            if food_times[i % len(food_times)] == 0:
                continue
            # food_times가 모두 다 0일 경우, -1return
            food_times[i % len(food_times)] -= 1
            k -= 1


print(solution([3, 1, 2], 5))
# print(solution([1, 0, 0], 5))
