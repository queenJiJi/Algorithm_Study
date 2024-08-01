from collections import Counter

def solution(clothes):
  answer = 1
  cases = [x[1] for x in clothes]
  print(cases)
  case_num = Counter(cases)
  print(case_num)

  for i in case_num:
    answer*=case_num[i]+1

  return answer -1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))