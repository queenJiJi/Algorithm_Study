'''
0: 홈, 1: 돌기

제한이 크지 않기 때문에 가능한 모든 경우를 탐색해 볼 수 있습니다. 
2차원 배열을 회전하는 함수를 하나 만들어 둔다면 코드를 더욱 깔끔하게 작성할 수 있습니다.

최대 4번까지 배열을 회전시키면서 가능한 경우를 모두 탐색한 다음, 
자물쇠의 모든 홈을 채워 비어있는 곳이 없도록 할 수 있다면 true를, 그렇지 않다면 false를 return 하면 됩니다.

key와 lock을 순서대로 맞춰보는 방법 중 하나는 
우선 lock 배열을 가로, 세로 길이가 3배인 새로운 배열의 중앙 부분으로 옮긴 후, 
key 배열을 새로운 배열의 좌측 상단부터 순서대로 이동시키면서 겹치는 부분만 확인해보면 됩니다.
이때, 겹치는 부분은 자물쇠의 모든 홈이 채워지더라도, 
겹치지 않는 부분에 여전히 자물쇠의 홈 부분이 남아있을 수 있으므로 모든 홈이 채워졌는지를 정확히 확인해야 합니다

아이디어 :
# 자물쇠의 행렬 변환(90º 돌리는 행위)을 구현해야 한다.
# key의 크기(M)은 항상 lock의 크기(N)이하라고 한다.
# lock의 크기를 3배 키운다.
# 입력으로 주어진 lock은 중앙에 배치한다.
# 키를 3배 키운 lock의 모든 자리에 대입한다.
# 만약 중앙에 위치한 lock이 모두 1이면 잠금이 해제된다.
# 그렇지 않으면 3배 키운 lock에 대입한 키를 다시 뺀다.
'''


def rotate_n_deg(arr):  # 오른쪽 90도를 n번 반복 -> 1번: 90도, 2번: 180도, 3번: 270도, 4번: 360도
    # new_A = arr
    # for _ in range(4):
    new_A = [i[::-1] for i in list(zip(*arr))]
    return new_A


def check(new_lock):  # 새 자물쇠판 내에 있는 자물쇠가 모두 1이 되었는지 확인
    lock_length = len(new_lock)//3
    for i in range(lock_length, lock_length*2):
        for j in range(lock_length, lock_length*2):
            if new_lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    n = len(lock)
    m = len(key)
    # 자물쇠의 크기를 기존의 3배로 변환
    new_lock = [[0]*(n*3) for _ in range(n*3)]
    # 새로운 자물쇠의 중앙 부분에 기존의 자물쇠 넣기 = 자물쇠를 가운데에 배치
    for r in range(n):
        for c in range(n):
            new_lock[r+n][c+n] = lock[r][c]
    # 4가지 방향에 대해서 확인:
    for rotation in range(4):
        key = rotate_n_deg(key)  # 열쇠회전
        for x in range(n*2):  # 한칸씩 이동하면서 확인
            for y in range(n*2):
                # 자물쇠에 열쇠를 끼어 넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                # 자물쇠에 열쇠가 정확히 들어맞는지 검사
                if check(new_lock) == True:
                    return True
                # 자물쇠에서 열쇠를 다시 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]

    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],
      [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
