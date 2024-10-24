from collections import deque

# BFS로 퍼즐 조각의 좌표 추출
def find_shape(board,x,y,value):
    n = len(board)
    q = deque()
    q.append((x,y))
    shape= [(x,y)] # 조각 저장
    board[x][y] = -1 # 방문 처리

    while q:
        r,c = q.popleft()

        for dx,dy in [[-1,0],[1,0],[0,-1],[0,1]]:
            nx,ny = dx+r, dy+c

            if 0<=nx<n and 0<=ny<n and board[nx][ny] == value:
                board[nx][ny] = -1 #방문처리
                q.append((nx,ny))
                shape.append((nx,ny))
    # 평등하게 비교해야하니까 정규화과정
    shape.sort() 
    min_x, min_y = shape[0][0], shape[0][1]
    normalized_shape = [(x-min_x, y-min_y) for x,y in shape]    
    return normalized_shape

# 90도 회전
def rotate(shape):
    return [(y,-x) for x,y in shape]

# 4방향 회전한 모든 모양 변환
def get_rotations(shape):
    rotations = []
    for _ in range(4):
        shape = rotate(shape)
        # 정렬해서 같은 모양 비교를 할 수 있게 정규화
        shape.sort()
        x_min,y_min=shape[0][0], shape[0][1]
        normalized_shape=[(x-x_min,y-y_min) for x,y in shape]
        rotations.append(normalized_shape)
    return rotations

def solution(game_board,table):
    n = len(game_board)

    # 1-1. 빈칸 모양 추출 (game_board에서 0인부분)
    empty_spaces = []
    for i in range(n):
        for j in range(n):
            if game_board[i][j] == 0:
                empty_spaces.append(find_shape(game_board,i,j,0))
    # 1-2. 퍼즐 모양 추출 (table에서 1인 부분)
    puzzle = []
    for i in range(n):
        for j in range(n):
            if table[i][j] == 1:
                puzzle.append(find_shape(table,i,j,1))

    # 2,3. 빈칸에 퍼즐 맞추기
    used = [False]*len(puzzle) # 사용된 퍼즐 추적
    answer = 0

    for empty in empty_spaces:
        empty_rotations = get_rotations(empty)

        for i, piece in enumerate(puzzle):
            if used[i]:
                continue # 이미 사용한 퍼즐이면 넘어가기

            piece_rotations = get_rotations(piece) 
            #  빈칸의 회전된 모양 중 하나가 퍼즐 조각의 회전된 모양 중 하나와 일치하는지 확인
            if any(rot in piece_rotations for rot in empty_rotations): # 4가지 방향으로 회전한 것 중 하나라도 일치하는 퍼즐이 있다면
                used[i] = True
                answer+=len(piece) # 퍼즐 조각 크기 만큼 채운 칸 추가
                break
    return answer

print(solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]],[[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]))
print(solution([[0,0,0],[1,1,0],[1,1,1]],[[1,1,1],[1,0,0],[0,0,0]]))