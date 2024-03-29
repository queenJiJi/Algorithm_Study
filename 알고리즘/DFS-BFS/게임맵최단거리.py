# 0: 벽이 있는 자리 ,1: 벽이 없는 자리
# start = (1,1)
# 상대 진영 :(n,m)
from collections import deque


def solution(maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    answer = 0

    def bfs(x, y):
        queue = deque()
        queue.append((x, y))

        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]

                if not (0 <= nx < len(maps) and 0 <= ny < len(maps[0])):
                    # if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps):
                    continue
                if maps[nx][ny] == 0:
                    continue
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y]+1
                    queue.append((nx, ny))
        # return maps[len(maps)-1][len(maps[0])-1]
    bfs(0, 0)
    return -1 if maps[4][4] == 1 else maps[4][4]


print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [
      1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))
