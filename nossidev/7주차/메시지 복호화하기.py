def solution(m,k):
  new_m = m+k
  l,r = 0, len(m)
  answer = ''

  while l<=r:
    if r>=len(new_m):
      break
    if new_m[l] == new_m[r]: # 값이 같을 경우
      l+=1 
      r+=1
    else: # 값이 다를 경우
      answer+=new_m[l]
      l+=1
 
  return answer+new_m[l:len(m)]

print(solution(m="lszxllcu",k="szl"))
print(solution(m="bjzyemrlht",k="bjyemrlht"))
print(solution(m="zbiaud",k="biaud"))
print(solution(m="yloiyqfvihdxiuevbryayldvb",k="xe"))