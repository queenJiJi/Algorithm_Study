# SOL1 - Queue
# from collections import deque
# def solution(queue1, queue2):
#   q1 = deque(queue1)
#   q2 = deque(queue2)
#   q1_sum = sum(q1)
#   q2_sum = sum(q2)
#   count = 0  
#   n = len(queue1)

#   for _ in range(0,3*n):
#     if q1_sum == q2_sum:
#       return count
#     elif q1_sum <q2_sum:
#       popped_item = q2.popleft()
#       q1.append(popped_item)
#       q1_sum+=popped_item
#       q2_sum-=popped_item
#       count+=1
#     else:  #sum(q1) > sum(q2):
#       popped_item = q1.popleft()
#       q2.append(popped_item)  
#       q1_sum-=popped_item
#       q2_sum+=popped_item
#       count+=1
#   return -1 

# SOL2 - Two Pointer
from collections import deque
def solution(queue1, queue2):
  q1,q2 = deque(queue1),deque(queue2)
  goal = (sum(q1) + sum(q2))//2
  que = q1+q2
  q1_sum = sum(q1)
  n = len(q1)
  i, j = 0, len(q1)

  for answer in range(0,3*n):
    if q1_sum > goal:
      q1_sum -= que[i]
      i+=1
    elif q1_sum < goal:
      q1_sum += que[j]
      j+=1
    else: # q1_sum == goal
      return answer
    if (i == j) or (j>=len(que)): # 두 포인터가 만나거나 j가 que보다 커질경우
      return -1
  


print(solution([3, 2, 7, 2],[4, 6, 5, 1]))
print(solution([1, 2, 1, 2],[1, 10, 1, 2]))
print(solution([1, 1],[1, 5]))