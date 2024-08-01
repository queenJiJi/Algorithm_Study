def solution(msg):
  answer = [0]
  n = len(msg)
  dic= {}
  for idx,ch in enumerate(range(65,91),start=1):
    dic[chr(ch)]= idx

  turn = 27
  w = ''
  for i in range(n):
    w+=msg[i]# 일단 새로운 것 붙이고

    if w not in dic:  # 그 단어가  없다면 
      dic[w] = turn # dic에 추가
      turn+=1

      w = msg[i] # 없었으니 원래 글자로
      answer.append(dic[w]) # 그 글자의 자리 정답에 붙이기 
    else: # 그 글자가 dic에 있다면
      answer[-1] = dic[w] # 마지막으로 붙여주기

  return answer

print(solution('KAKAO'))
print(solution('TOBEORNOTTOBEORTOBEORNOT'))
print(solution('ABABABABABABABAB'))