def solveSudoku(board):
    # num이 row 행, col 열에 배치 가능한지 확인하는 함수
    def is_valid(num, row, col):
        # 3x3 박스의 인덱스를 계산
        box_index = (row // 3) * 3 + col // 3
        # 해당 숫자가 이미 해당 행, 열 또는 박스에 존재하는지 확인
        return not (num in rows[row] or num in cols[col] or num in boxes[box_index])

    # num을 row 행, col 열에 배치하는 함수
    def place_number(num, row, col):
        box_index = (row // 3) * 3 + col // 3
        rows[row].add(num)    # 해당 행에 숫자 추가
        cols[col].add(num)    # 해당 열에 숫자 추가
        boxes[box_index].add(num)  # 해당 박스에 숫자 추가
        board[row][col] = num  # 보드에 숫자 배치

    # row 행, col 열에서 num을 제거하는 함수
    def remove_number(num, row, col):
        box_index = (row // 3) * 3 + col // 3
        rows[row].remove(num)    # 해당 행에서 숫자 제거
        cols[col].remove(num)    # 해당 열에서 숫자 제거
        boxes[box_index].remove(num)  # 해당 박스에서 숫자 제거
        board[row][col] = '.'  # 보드에서 숫자 제거

    # 백트래킹 함수: row 행, col 열에서 시작하여 숫자를 채움
    def backtrack(row=0, col=0):
        # 모든 행을 다 채웠다면 (0부터 8까지), 퍼즐이 해결된 것
        if row == 9:
            return True
        # 마지막 열까지 채웠다면 다음 행으로 이동
        if col == 9:
            return backtrack(row + 1, 0)
        # 이미 숫자가 채워져 있는 칸이면 다음 칸으로 이동
        if board[row][col] != '.':
            return backtrack(row, col + 1)

        # 숫자 1부터 9까지 시도
        for num in '123456789':
            # 현재 위치에 num을 배치할 수 있는지 확인
            if is_valid(num, row, col):
                place_number(num, row, col)  # num을 배치
                if backtrack(row, col + 1):  # 다음 칸으로 이동
                    return True
                remove_number(num, row, col)  # 배치 실패 시 num을 제거
        return False

    # 각 행, 열, 박스에 이미 존재하는 숫자를 추적하기 위한 집합 리스트
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    # 보드 초기 상태에서 이미 채워져 있는 숫자들로 집합 초기화
    for r in range(9):
        for c in range(9):
            if board[r][c] != '.':
                place_number(board[r][c], r, c)

    backtrack()  # 백트래킹 시작

# 입력 예시
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

solveSudoku(board)
# 보드의 결과 출력
for row in board:
    print(row)
