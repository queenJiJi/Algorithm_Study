def solution(s):
  str_len = len(s)
  answer = str_len

  # 순차적으로 문자열의 반만큼 잘라주기
  for size in range(1,str_len//2+1):
    words = [s[i:i+size] for i in range(0,str_len,size)]
    stack = [[words[0],1]]
    # 자른 것들의 패턴 찾기
    for word in words[1:]:
      if word == stack[-1][0]:
        popped = stack.pop()
        stack.append([popped[0],popped[1]+1])
      else:
        stack.append([word,1])
    # 압축 문자열 만들기
    compressed = ''.join([str(cnt)+w if cnt>1 else w for w,cnt in stack])
    # 압축 문자열 중에 길이가 최소인것 구하기
    answer = min(answer, len(compressed))
  return answer


print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))