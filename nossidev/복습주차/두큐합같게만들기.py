# q1의 시작, q2의 시작 : l,r
# q를 하나로 합치기
from collections import deque

def solution(queue1,queue2):
  q1 = deque(queue1)
  q2 = deque(queue2)

  l,r=0,len(q1)

  q = q1+q2+q1
  n = len(q)
  target = (sum(q1)+sum(q2))//2
  q1_sum = sum(q1)
  q2_sum = sum(q2)
  count = 0

  for _ in range(n):
    # if l==r or r>len(q):
    #   return -1
    if q1_sum == q2_sum:
      return count 
    elif q1_sum > q2_sum:
      popped_item = q1.popleft()
      q2.append(popped_item)
      q1_sum -= popped_item
      q2_sum += popped_item
      count +=1
    else:
      popped_item = q2.popleft()
      q1.append(popped_item)
      q2_sum -= popped_item
      q1_sum += popped_item
      count +=1
  return -1 

  #   if target == q1_sum:
  #     return count
    
  #   elif target > q1_sum:
  #     q1_sum += q[r]
  #     r+=1
  #   else:
  #     q1_sum -= q[l]
  #     l+=1
  # return -1


print(solution([3, 2, 7, 2],	[4, 6, 5, 1]))
print(solution([1, 2, 1, 2],	[1, 10, 1, 2]))
print(solution([1,1],	[1,5]))