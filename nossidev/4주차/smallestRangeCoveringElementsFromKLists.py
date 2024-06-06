#✅ nums[idx]의 원소들이 몇 번째 리스트에 속해있는지 알기 쉽도록 "값 => [값, idx]" 변경한다

#✅ 각 리스트의 첫 번째 원소들을 우선순위 큐에 입력한다.
	#✅ 입력하는 과정 중 원소들의 최댓값을 기록한다.

#✅ 우선순위 큐로 얻은 최솟값과 기록된 최댓값을 통해 범위를 기록한다.
#✅ 우선순위 큐에서 제거된 값이 존재하던 리스트에서 다음 값을 찾아 우선순위 큐에 저장한다.
	#✅ 입력하는 과정 중 최댓값을 갱신한다.

#✅ 각 리스트의 원소 중 한 원소가 마지막 값에 도달할 때까지 반복한다.
import heapq

def solution(nums):
  n = len(nums)
  # 트래킹이 편하게 각 원소들이 속한 리스트의 인덱스값을 달아줌
  for i in range(n):
    nums[i] = [[val,i] for val in nums[i]]

  pq =[]
  max_val = -float('inf')

  for i in range(n): # 우선 각 리스트들의 가장 첫번째 원소를 힙에 넣어주고, max_val 값도 만들어줌 
    heapq.heappush(pq,nums[i][0])
    max_val = max(max_val, nums[i][0][0])
  
  answer = [pq[0][0],max_val] # 범위를 return해줄 answer 값 초기화
  index_list = [0] * len(nums) # 리스트 트래킹과 종료조건을 위함

  while 1:
    min_val, idx = heapq.heappop(pq)
    index_list[idx] += 1

    # 종료조건
    if index_list[idx] == len(nums[idx]):
      break
    
    next_num = nums[idx][index_list[idx]] # 하나를 뺐으니, 다음으로 넣어줄 수= 빠진 값이 있던 리스트에서 다음 원소를 가져옴
    heapq.heappush(pq, next_num) # 그 원소를 넣어주고
    max_val = max(max_val, next_num[0]) # 방금 넣어준 원소와 max값을 비교

    # 바뀐 range와 원래 answer과 비교해서 더 작은 range값을 갖고 있다면 answer를 갱신  
    if max_val - pq[0][0] < answer[1]-answer[0]:
      answer = [pq[0][0],max_val]

  return answer



print(solution([[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]))
print(solution([[1,2,3],[1,2,3],[1,2,3]]))