def solution(plans):
  answer = []
  stack= []
  n = len(plans)
  plans.sort(key=lambda x:(x[1]))
  for i in range(n):
    h,m = plans[i][1].split(':')
    plans[i][1] = int(h)*60+int(m) 
    plans[i][2] = int(plans[i][2])

  for i in range(n-1):
    stack.append([plans[i][0],plans[i][2]])
    gap = plans[i+1][1] - plans[i][1]

    while stack and gap:
     # stack[-1][1] = 현재 과제의 소요시간
      if gap >= stack[-1][1]: # 다음 과목 시작전내에 현재 과목을 끝낼 수 있다면
          subject, take = stack.pop()
          gap-=take
          answer.append(subject) # 과제 완료
      else: # 다음 과목 시작전 내에 현재 과목을 끝낼 수 없다면
          stack[-1][1] -= gap # 다음 과제 시작전까지 현재과제 수행
          gap = 0 # 다음 과제를 시작해야하니까 0으로 초기화
  answer.append(plans[-1][0]) # 마지막 과목은 어짜피 이때까지 오면 끝낼때까지 해줘야하니 answer에 넣어주기

  for i in range(len(stack)): # stack에 남아있는 것들 처리
    answer.append(stack[~i][0]) # 이렇게하면 역순으로 붙음 

  return answer

print(solution([["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]))
print(solution([["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]))
print(solution([["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]]))