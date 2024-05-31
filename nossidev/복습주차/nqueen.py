def solution(n):
  result = []
  cols,rightDiag,leftDiag = set(),set(),set()
  board=[['.']*n for _ in range(n)]

  def backtrack(row):
    # base case
    if row == n:
      print(board)
      copy_row = [''.join(r) for r in board]
      result.append(copy_row)
      return
    
    for col in range(n):
      # 퀸을 놓지 못하는 조건
      if (col in cols or (row+col) in leftDiag or (row-col) in rightDiag):
        continue

      cols.add(col)
      leftDiag.add(row+col)
      rightDiag.add(row-col)
      board[row][col] = 'Q'
      backtrack(row+1)
      cols.remove(col)
      leftDiag.remove(row+col)
      rightDiag.remove(row-col)
      board[row][col] = '.'
  backtrack(0)
  return result 


print(solution(4))
print(solution(1))