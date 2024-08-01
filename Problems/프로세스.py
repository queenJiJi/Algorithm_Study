def solution(priorities,location):
  answer= 0
  q=[[idx,val] for idx,val in enumerate(priorities)]
  
  while True:
    cur_node = q.pop(0)

    if any(cur_node[1]<i[1] for i in q):
      q.append(cur_node)
    else:
      answer+=1
      if cur_node[0] == location:
        return answer        

print(solution([2,1,3,2],2))
print(solution([1,1,9,1,1,1],0))