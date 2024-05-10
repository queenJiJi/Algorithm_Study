# sol1 - bfs
from collections import deque
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
n,m = len(board[0]), len(board[0][0])

def solution():
  # 우, 하, 좌, 상 
  dr = [0,1,0,-1]
  dc = [1,0,-1,0]
  dir = 0

  arr= []
  start = board[0][0]

  while 1:
    r,c = 0,0

    for i in range(4):
      nr = r + dr[dir]
      nc = c + dc[dir]
      if nr<0 or nc<0 or nr>=n or nc>=n:
        break



