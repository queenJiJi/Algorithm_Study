def solution(m, n, board):
    answer = 0
    block = set()
    board = [list(row) for row in board]
    
    while 1:
        for r in range(m-1):
            for c in range(n-1):
                b = board[r][c]
                if b == []:
                    continue
                if b == board[r+1][c] and b == board[r][c+1] and b==board[r+1][c+1]:
                    block.add((r+1,c))
                    block.add((r,c+1))
                    block.add((r+1,c+1))
                    block.add((r,c))
        if not block:
            break
            
        answer+=len(block)
        for r,c in block:
            board[r][c] = []
        block = set()
    
        while 1:
            moved = 0
            for r in range(m-1,0,-1):
                for c in range(n):
                    if board[r][c] == [] and board[r-1][c]!= []:
                        board[r][c] = board[r-1][c]
                        board[r-1][c] = []
                        moved = 1
            if moved == 0:
                break

    return answer