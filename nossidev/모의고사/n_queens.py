def solveNQueens(n):
        board = [['.']*n for _ in range(n)]
        cols, leftDiag, rightDiag = set(),set(),set()
        result = []
        def backtrack(row):
            # base case
            if row == n:
                copy_row = [''.join(r) for r in board]
                result.append(copy_row)
                return

            for col in range(n):
                # 놓을 수 없는 케이스
                if (col in cols or (col-row) in rightDiag or (col+row) in leftDiag):
                    continue
                
                cols.add(col)
                rightDiag.add(col-row)
                leftDiag.add(col+row)
                board[row][col] = 'Q'
                backtrack(row+1)
                cols.remove(col)
                rightDiag.remove(col-row)
                leftDiag.remove(col+row)
                board[row][col] = '.'
        backtrack(0)
        return result