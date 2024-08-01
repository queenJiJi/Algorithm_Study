def div(yellow):
  cases = []
  if yellow==1:
    cases.append([1,1])
    return cases
  else:
    for i in range(1,yellow):
      if yellow%i==0:
        cases.append([yellow//i,i])
    return cases
def solution(brown, yellow):
 
  for ga,se in div(yellow):
    # print(ga,se)
    if ga>=se:
      if (ga*2+se*2+4) == brown:
        return [ga+2,se+2]


print(solution(10,2))
print(solution(8,1))
print(solution(24,24))