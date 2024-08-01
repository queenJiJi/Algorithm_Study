from heapq import heapify, heappop, heappush
def solution(scoville,K):
  cnt = 0
  s= scoville
  heapify(s)
  
  while 1:
    if s[0] > K:
      return cnt
    if len(s) == 0:
      return -1
    lowest = heappop(s)
    next_lowest = heappop(s)

    heappush(s,(lowest+next_lowest*2))
    cnt+=1
  return cnt
print(solution([1,2,3,9,10,12],7))