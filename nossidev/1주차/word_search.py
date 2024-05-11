board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"


def solution():
  n = len(board)
  m = len(board[0])
  path = set()
  def dfs(r,c,cur_word_idx):
        # 탈출 조건: word의 끝까지 다 확인했으면 나오기
        if cur_word_idx == len(word):
            return True
        # 안되는 조건 
        if (r<0 or c<0 or r>=n or c>=m or # out of range이거나
            word[cur_word_idx] != board[r][c] or # 찾는 단어랑 보드에 있는 단어가 일치하지 않거나
            (r,c) in path): # 이미 방문한 곳을 또 방문하려고 한다면
            return False
        # 문제가 없다면
        path.add((r,c)) # 해당 letter를 path에 추가
        # 상,하,좌,우 다 살핌
        result = (dfs(r+1,c,cur_word_idx+1) or 
                dfs(r-1,c,cur_word_idx+1) or 
                dfs(r,c-1,cur_word_idx+1) or 
                dfs(r,c+1,cur_word_idx+1))

        path.remove((r,c))
        return result
  

 
  # 보드 내부를 돌면서 하나씩 확인
  for r in range(n):
    for c in range(m):
        if dfs(r,c, 0): # 어떤 결과값이 나온다면
            return True
  # 루프를 다 돌았는데도 일치하는게없다면
  return False



print(solution())