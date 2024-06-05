import heapq
# 작업이 요청되는 시점이 빠른 순서로 정렬한다.

'''
현재 시점에서 처리할 수 있는 작업들을 힙에 넣고, 하나를 뽑아 현재 시점과 총 대기시간을 구해주는 것을 모든 작업을 처리할 때까지 반복한다.

힙에 push를 할 때는 작업의 소요 시간 기준으로 최소힙이 만들어져야 하기 때문에 jobs의 요소를 그대로 넣지 않고 
[작업의 소요 시간, 작업이 요청되는 시점]으로 요소의 앞 뒤를 바꿔서 넣어준다.

현재 시점에서 처리할 수 있는 작업인지를 판별하는 조건은
 작업의 요청 시간이 바로 이전에 완료한 작업의 시작 시간(start)보다 크고 현재 시점(now)보다 작거나 같아야 한다.

만약 현재 처리할 수 있는 작업이 없다면,
남아 있는 작업들의 요청 시간이 아직 오지 않은 것이기 때문에 현재 시점(now)을 하나 올려준다.
'''
def solution(jobs):
  answer, now, job_cnt = 0,0,0
  start = -1 
  pq =[]

  while job_cnt < len(jobs): # 모든 디스크를 다 처리할 때까지 
    for job in jobs:
      if start < job[0] <= now: # 현재 시점에서 처리할 수 있는 작업인지 판별하는 조건 
        heapq.heappush(pq, (job[1],job[0])) # 소요시간이 작은 것 부터 빼줄 것이기때문에 소요시간을 기준으로 넣어주기위해 순서바궈서 넣기

    if pq: # 처리할 작업이 있다면
      cur_disc_duration, cur_disc_start = heapq.heappop(pq)
      start = now  # 시작시간을 현재 시간으로 갱신 
      now += cur_disc_duration # 현재시간에 작업 소요시간을 더해서 현재 시간 갱신
      answer += (now - cur_disc_start) # answer에 요청부터 종료까지의 시간 갱신(현재시간-요청시작시간)
      job_cnt +=1 #일 하나 처리했으므로 +1
    else: #처리할 작업이 없는 경우 현재 시간 1 증가
      now +=1
  return answer//len(jobs)


print(solution([[0, 3], [1, 9], [2, 6]]))




