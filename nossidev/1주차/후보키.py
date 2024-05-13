from itertools import combinations

def solution(relation):

  cor_len = len(relation[0])
  row_len = len(relation)

  candidate_keys = []
  for length in range(1, cor_len+1):
    # 속성 개수 별로 모든 조합을 만들기
    for cols in combinations(range(cor_len), length):
      minimality = True # 
      row_set = set()

      # 최소성 검사
      for key in candidate_keys:
        if set(key).issubset(cols): 
          minimality = False
          break
      if not minimality: # 만약 최소성 만족 못할시 
        continue # 정답 후보군에 넣어주지 않고 다음 속성 조합의 후보키 검색 진행

      # 유일성 검사
      for r in range(row_len):
        row_str = ''
        for c in cols:
          row_str += relation[r][c]
        row_set.add(row_str)

      if len(row_set) == row_len: # 튜플 간 중복이 없으면 해당 속성 조합을 후보키에 포함 
        candidate_keys.append(cols)


  return len(candidate_keys) 

print(solution(relation=[["100","ryan","music","2"],
                         ["200","apeach","math","2"],
                         ["300","tube","computer","3"],
                         ["400","con","computer","4"],
                         ["500","muzi","music","3"],
                         ["600","apeach","music","2"]]))

