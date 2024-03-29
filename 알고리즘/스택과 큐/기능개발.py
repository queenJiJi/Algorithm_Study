from collections import deque


def solution(p, s):
    queue = deque()
    count = 1  # 배포 기능의 개수를 세는 변수
    answer = []

    for i in range(len(p)):
        if (100-p[i]) % s[i] != 0:
            queue.append(((100-p[i])//s[i])+1)
            # print(((100-p[i])//s[i])+1)
        else:
            queue.append((100-p[i]) // s[i])
            # print((100-p[i]) // s[i])

    # 첫번째 작업의 남은 일 수
    prev = queue.popleft()
    # 남은 작업이 없을 때 까지 반복 = 큐가 비기 전까지 반복
    while queue:
        # 다음 작업의 남은 일 수
        current = queue.popleft()
        # 이전 작업이 현재 작업의 남은 일수가 더 크다면,
        # 이전까지의 배포되는 기능의 개수를 결과에 추가하고
        if prev >= current:
            count += 1
        # 크지않다면
        else:
            answer.append(count)  # answer배열에 추가
            count = 1  # count초기화
            prev = current  # 이전일이 현재 일이됨

    # 마지막으로 남은 기능의 배포 개수 추가
    answer.append(count)
    return answer  # answer return


print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))

# 계산된 남은 일수를 이용하여 각 배포마다 몇 개의 기능이 배포되는지 구합니다.
# 첫 번째 기능부터 순서대로 남은 일수를 비교하면서 배포되는 기능의 개수를 세면 됩니다.
# 만약 현재 기능의 남은 일수가 다음 기능의 남은 일수보다 크다면,
# 현재까지 센 배포되는 기능의 개수를 결과 리스트에 추가하고,
# 배포되는 기능의 개수를 초기화합니다.
