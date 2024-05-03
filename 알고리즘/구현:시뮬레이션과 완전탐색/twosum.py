'''
  https://leetcode.com/problems/two-sum/submissions/1240601205/
  리스트 [4,9,7,5,1]에서 2개의 숫자를 더해서 15가 될 수 있나요? (중복x)

  이 two sum 문제를 원래는 dic으로 풀었었다.
  하지만 만약 2개의 합이 아니라 k개의 합이 된다면 for loop를 무한히 많이 써야할 수도 있다.
  이럴땐 backtracking을 사용하자
'''

# original sol
def original(target, nums):
  n = len(nums)
  for i in range(n):
    for j in range(i+1, n):
      if i==j:
        break
      if nums[i]+nums[j]==target:

        return [i,j]

print(original(target = 13,nums =[4,9,7,5,1]))    


# backtracking sol
def sol(target, nums, k):
  def backtracking(start, curr):
    if len(curr) == k and sum(nums[i] for i in curr) == target:
      return curr
    
    for i in range(start, len(nums)):
      curr.append(i)
      result = backtracking(i+1, curr)
      
      if result != None:
        return result
      
      curr.pop()
    return None
  return backtracking(0,[])

print(sol(target=15, nums =[4,9,7,5,1], k =3))