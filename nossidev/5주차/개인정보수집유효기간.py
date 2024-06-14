def solution(today, terms, privacies):
  answer = []

  #모든 날짜를 가장 최소단위인 ‘일’에 맞춰서 계산해주기 
  def dateChange(date):
    return (int(date[0])*28*12-2000) + (int(date[1])*28) + (int(date[2])) # 년 월 일 # 어짜피 2000년 이상 부터 시작이니까 2000빼고 시작하기
  
  # 약관 종류에 따라 해시맵으로 유효기간 설정해주기 
  term_dic = {}
  for t in terms:
    term,due = t.split()
    term_dic[term] = int(due) * 28 # key: 약관종류 , val: 유효기간(일 기준) 

  # 현재날짜 - 보관일자 > 0 라면 폐기해야하는 것이므로 해당 privacy는 +1
  for idx, privacy in enumerate(privacies):
    collected_date, term = privacy.split()
    collected_day = dateChange(collected_date.split('.')) + term_dic[term]
    now = dateChange(today.split('.'))
    if now-collected_day >= 0:
      answer.append(idx+1)  # 인덱스가 1부터 시작이라

  return answer

print(solution("2022.05.19",	["A 6", "B 12", "C 3"],	["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]	))
print(solution("2020.01.01",	["Z 3", "D 5"],	["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]	))