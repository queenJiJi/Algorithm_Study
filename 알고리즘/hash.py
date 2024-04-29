def solution(nums):
  answer = 0
  nums_dict= {}
  for i in nums:
    nums_dict[i] = True

  for num in nums_dict:
    if num-1 not in nums_dict: # 즉, num이 consecutive의 첫시작수일때
      count =1 
      target = num+1
      while target in nums_dict:
        count +=1
        target = target+1
      answer = max(answer,count)
  return answer





print(solution([100,4,200,1,3,2]))
print(solution([0,3,7,2,5,8,4,6,0,1]))
