def solution(board,word):
  n = len(word)
  row_len, col_len = len(board),len(board[0])
  visited = [[False]*col_len for _ in range(row_len)]
  def backtrack(cur_r,cur_c, w_idx):
    # 탈출조건
    if w_idx == n:
      return True
    
    if not(0<=cur_r<row_len and 0<=cur_c<col_len) or visited[cur_r][cur_c] or board[cur_r][cur_c]!=word[w_idx]:
      return False

    visited[cur_r][cur_c] = True
    for dr,dc in [[-1,0],[1,0],[0,1],[0,-1]]:
      nr,nc = dr+cur_r, dc+cur_c 
      if backtrack(nr,nc,w_idx+1):
        return True
    visited[cur_r][cur_c] = False

  for r in range(row_len):
    for c in range(col_len):
      if backtrack(r,c,0):
        return True
  return False

print(solution(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"))
print(solution(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"))
print(solution(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"))
print(solution(board=[["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], word="ABCESEEEFS"))