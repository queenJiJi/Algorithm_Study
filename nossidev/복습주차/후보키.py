# 완전탐색으로 가능한 모든 경우의 수를 다 갖고, 해당 경우의 수가 유일성과 최소성을 만족하는 경우 reulst에 포함 시키는 것
'''
컬럼으로 만들 수 있는 모든 부분집합을 구해서 
  그 부분 집합 중 유일성이 만족하는 집합 -? 
   그 중 최소성을 만족하는 집합만 정답 처리 -?
'''
from itertools import combinations

def solution(relation):
  row_len, col_len = len(relation), len(relation[0])
  result= []
  for col in range(1,col_len+1):
    for comb in combinations(range(col_len),col):
      minimality = True
      candidate = set()
      # 최소성
      for key in result:
        if set(key).issubset(comb):
          minimality = False
          break
      if not minimality:
        continue

      # 유일성
      for r in range(row_len):
        row_str= ''
        for c in comb:
          row_str+=relation[r][c]
        candidate.add(row_str)
      if len(candidate) == row_len:
        result.append(comb)

  return len(result)



print(solution([["100","ryan","music","2"],
                ["200","apeach","math","2"],
                ["300","tube","computer","3"],
                ["400","con","computer","4"],
                ["500","muzi","music","3"],
                ["600","apeach","music","2"]]))