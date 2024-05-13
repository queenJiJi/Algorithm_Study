from collections import defaultdict

# def isValid(board):
#     cols = defaultdict(set)
#     rows = defaultdict(set)
#     box = defaultdict(set)

#     for r in range(9):
#         for c in range(9):
#             if board[r][c] == '.':
#                 continue
#             if (board[r][c] in rows[r] or
#                 board[r][c] in cols[c] or
#                 board[r][c] in box[(r//3, c//3)]):
#                 return False
#             cols[c].add(board[r][c])
#             rows[r].add(board[r][c])
#             box[(r//3, c//3)].add(board[r][c])
#     return True

# def isEmpty(board,r,c):
#     if board[r][c] == '.':
#         return True
#     return False

# def solution(board):
#     def backtrack(board, cur_idx):
#         if cur_idx == 81:
#             return True

#         r, c = divmod(cur_idx, 9)

#         if isEmpty(board,r,c):
#           # 칸이 비어있는 경우 
#           for num in map(str, range(1, 10)):
#               board[r][c] = num
#               # if isValid(board) and backtrack(board, cur_idx+1):
#               #     return True
#               if isValid(board):
#                   if backtrack(board,cur_idx+1):
#                     return True   
#               board[r][c] = '.'
#         else: # 칸에 이미 숫자가 있는 경우
#             return backtrack(board,cur_idx+1) # 다음칸으로 넘어가기
    
#     backtrack(board, 0)
#     return board

def isValid(board):
    cols=defaultdict(set)
    rows=defaultdict(set)
    box=defaultdict(set)
    for r in range(9):
        for c in range(9):
            if board[r][c] == '.':
                continue
            if (board[r][c] in cols[c] or
                board[r][c] in rows[r] or
                board[r][c] in box[(r//3),(c//3)]):
                return False
            cols[c].add(board[r][c])
            rows[r].add(board[r][c])
            box[(r//3, c//3)].add(board[r][c])
    return True

def isEmpty(board,r,c):
    if board[r][c] == '.':
        return True
    return False

def solution(board):
    def backtrack(board,cur_idx):
        if cur_idx == 81:
            return True

        r,c= divmod(cur_idx,9)
        
        if isEmpty(board,r,c):
            for num in map(str,range(1,10)):
                board[r][c] = num
                if isValid(board) and backtrack(board,cur_idx+1):
                    return True
                board[r][c] = '.'
        else:
            return backtrack(board,cur_idx+1)
    backtrack(board, 0)
    return board

# Example usage:
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
print(solution(board))
