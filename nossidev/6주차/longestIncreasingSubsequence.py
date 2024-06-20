from bisect import bisect_left
def solution(nums):
  # SOL 1 - DP
  dp= [1]* len(nums) # 아무리 길이가 짧아도 본인 길이1일테니까 dp테이블의 원소를 모두 1로 초기화

  for i in range(1,len(nums)):
    for j in range(0,i):
      if nums[i]>nums[j]:
        dp[i] = max(dp[i], dp[j]+1)
  return max(dp)

  # SOL 2 - 정렬(이진탐색) 
  arr = [] # Longest Increasing Subsequence를 저장할 리스트
  for num in nums:
    index = bisect_left(arr,num) # arr내에 num이 들어갈 위치를 찾음

    if len(arr) == index: # num이 들어갈 위치가 arr의 끝이면, arr에 추가
      arr.append(num)
    else: # 그렇지 않으면, 해당 위치 값에 num으로 대체
      arr[index] = num
  return len(arr) # 최종 arr의 길이가 LIS의 길이임

print(solution(nums = [10,9,2,5,3,7,101,18]))
print(solution(nums = [0,1,0,3,2,3]))
print(solution(nums = [7,7,7,7,7,7,7]))