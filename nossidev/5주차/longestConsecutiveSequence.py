def solution(nums):
  hashset = set(nums)
  count, answer = 0 , 0

  for val in hashset:
    prev = val - 1 # 항상 첫 시작점일 때만 loop를 돌게해서 중복 없애기
    if prev not in hashset: # (1,2,3일때 1만 해도 됨 2,3은 1에서 이미 할테니까)
      count = 1
      next = val +1 # 다음값 
      while next in hashset: # 다음값이 hashset이 존재할때까지
        count += 1 # 얼마나 긴지 확인하기 위한 변수
        next += 1 # 또 다음값으로 넘어가기
      answer = max(answer, count)
  return answer 

print(solution([100,4,200,1,3,2]))
print(solution([0,3,7,2,5,8,4,6,0,1]))

