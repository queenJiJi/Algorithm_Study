def solution(s):
  charSet = set()
  left = 0
  answer = 0
  for right in range(len(s)): # right pointer를 하나씩 오른쪽으로 옮겨주기
    while s[right] in charSet: # 오른쪽 포인터가 가르키는 글자가 이미 charset에 있다면 = 중복이라면 즉, 중복이 사라질때까지 반복
      charSet.remove(s[left]) # 왼쪽 글자 set에서 없애주기
      left+=1 # 포인터 이동
    charSet.add(s[right]) # 그 오른쪽 값 추가
    answer = max(answer, right-left+1) # 길이 update
  return answer


print(solution("abcabcbb"))
print(solution("bbbbb"))
print(solution("pwwkew"))