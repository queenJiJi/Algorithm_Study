from heapq import heappop, heappush

val = [5,10,1,4,2,3,5,2]
heap=[]

for v in val:
  if not heap:
    heappush(heap,(v))
    print(heap)
    continue
  if heap[0]<v:
    print(v)
    heappop(heap)
  heappush(heap,(v))

# 실시간으로 오름차순 정렬됨
# 결국 끝에 heap에 남은 것 : [2,4,5,10]