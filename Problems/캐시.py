from collections import defaultdict, deque, Counter
def solution(cacheSize, cities):
  time =0
  q=deque(maxlen=cacheSize)

  for c in cities:
    c=c.lower()
    if c not in q:
      q.append(c)
      time+=5
    else:
      q.remove(c)
      q.append(c)
      time+=1
  return time

print(solution(3,	["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))