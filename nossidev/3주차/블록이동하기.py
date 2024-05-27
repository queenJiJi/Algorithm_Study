from collections import deque

def next_move(cur_pos,new_board):
    next_pos = []
    pos = list(cur_pos)
    lx,ly,rx,ry = pos[0][0],pos[0][1],pos[1][0],pos[1][1]
    #상하좌우 이동이 가능한 경우를 구한다.
    for dr,dc in [[-1,0],[1,0],[0,-1],[0,1]]:
      nlx,nly,nrx,nry = lx+dr,ly+dc, rx+dr, ry+dc  
      if new_board[nlx][nly] == 0 and new_board[nrx][nry] == 0:
        next_pos.append([(nlx,nly),(nrx,nry)])
    #가로 방향일 경우 회전 가능한 경우를 구한다.
    if lx==rx:
      for i in [-1,1]:
        if new_board[lx+i][ly] == 0 and new_board[rx+i][ry] == 0:
          next_pos.append([(lx ,ly),(lx+i,ly)])
          next_pos.append([(rx ,ry),(rx+i,ry)])
    #세로 방향일 경우 회전 가능한 경우를 구한다.
    if ly == ry:
      for i in [-1,1]:
        if new_board[lx][ly+i] == 0 and new_board[rx][ry+i] ==0:
          next_pos.append([(lx,ly),(lx,ly+i)])
          next_pos.append([(rx,ry),(rx,ry+i)])
    return next_pos


def solution(board):
  result = 0
  n = len(board)
  #인덱싱의 편의를 위해 원본 배열에 상하좌우로 한 칸씩 늘린 새 배열을 만든다.
  new_board = [[1]* (n+2) for _ in range(n+2)]
  #배열의 모서리 부분을 1로 채우고 내부를 원본 배열의 값들로 채운다.
  for i in range(n):
    for j in range(n):
      new_board[i+1][j+1] = board[i][j]

  visited = set()
  q = deque()

  #로봇의 첫 위치를 방문표시하고 큐에 추가한다.
  robot_pos = set([(1,1),(1,2)])
  q.append((robot_pos,0))
  visited.add(frozenset(robot_pos))
  #큐가 빌때까지 반복한다.
  while q:
    cur_pos, time = q.popleft()
    #목적지에 도착한 경우 종료한다.
    if (n,n) in cur_pos:
      return time
    #현재 상태에서 이동가능한 상태를 구한다.
    for next_pos in next_move(cur_pos,new_board):
      # 아직 방문하지 않았다면 방문한다.
      if frozenset(next_pos) not in visited:
        q.append((next_pos,time+1))
        visited.add(frozenset(next_pos))
  return -1 # 목적지에 도착하지 못한 경우는 없지만 실패 체크를 위해


print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))


