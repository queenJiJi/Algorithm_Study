def solution(board,word):
  n,m = len(board),len(board[0])
  
  visited = set()
  def dfs(r,c,idx):

    if len(word) == idx:
      return True
    
    if not (0<=r<n and 0<=c<m) or (r,c) in visited or word[idx] != board[r][c]:
      return False

    visited.add((r,c))
    for dr,dc in [[-1,0],[1,0],[0,-1],[0,1]]:
      nr,nc = r+dr, c+dc
      if dfs(nr,nc,idx+1):
        return True
    visited.remove((r,c))

  for r in range(n):
    for c in range(m):
      if dfs(r,c,0):
        return True
  return False
  

print(solution(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"))
  