def solution(n):
  result = []
  cols = set() 
  rightDiag= set() # r-c
  leftDiag= set() # r+c
  board = [['.']*n for _ in range(n)]
  def backtrack(row):
    # base case
    if row == n:
      copy_row = [''.join(row) for row in board]
      # print('h2i',[row for row in board])
      result.append(copy_row)
      return 
    
    # 전체적인 col을 돌면서 확인
    for col in range(n):

      # 퀸을 놓지 못하는 조건
      if col in cols or (row-col) in rightDiag or (row+col) in leftDiag:
        continue

      # 놓을 수 있는 조건이라면
      cols.add(col)
      rightDiag.add(row-col)
      leftDiag.add(row+col)
      board[row][col] = 'Q'
      backtrack(row+1)
      cols.remove(col)
      rightDiag.remove(row-col)
      leftDiag.remove(row+col)
      board[row][col] = '.'

      
  backtrack(0)
  return result
  

print(solution(n=4))
