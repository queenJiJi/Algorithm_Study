def solution(nums, target):
  hash = {}
  n = len(nums)

  for i in range(n):
    complement = target-nums[i]
    if complement in hash: # 보수가 hash에 존재한다면(=해당 보수를 key로 갖는 값이 있다면
      return [hash[complement],i] # 그 보수의 인덱스와 현재 인덱스를 반환
    else: # 해당 보수가 존재하지 않는다면,
      hash[nums[i]] = i # 키값을 원소로, val을 그 원소의 인덱스로 hash에 저장


print(solution(nums = [2,7,11,15], target = 9))
print(solution(nums = [3,2,4], target = 6))
print(solution(nums = [3,3], target = 6))