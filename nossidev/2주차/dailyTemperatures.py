def solution(temperatures):
  ans = [0] * len(temperatures)
  stack = []
  for idx,val in enumerate(temperatures):
    while stack and stack[-1][1] < val:
      prev_day = stack.pop()[0] # 현재 수보다 더 작은 수들을 모두 stack에서 pop해주고 그 pop한 값들의 날짜
      ans[prev_day] = idx-prev_day # 얼마나 현재 날(더 높은 수가 나온 당일)과 stack에서 더 높은 수가 나올때가지 기다린 날의 차이 업데이트
    stack.append((idx,val))     #현재 값보다 더 작은 값들이라면 stack에 넣어주기
  return ans

print(solution([73,74,75,71,69,72,76,73]))
print(solution([30,40,50,60]))
print(solution([30,60,90]))



