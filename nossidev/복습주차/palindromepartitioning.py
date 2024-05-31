# 모든 가능한 조합을 만들어서 - 그 중 palindrome인지 확인하기 
def solution(s):
  n = len(s)
  ans,result = [], []  

  def backtrack(start):
    # base case
    if start == n:
      result.append(ans[:])

    for i in range(start,n):
      substr = s[start:i+1]
      if substr == substr[::-1]:
        ans.append(s[start:i+1])
        backtrack(i+1)
        ans.pop()
    return result
  return backtrack(0)


print(solution('aab'))
print(solution('a'))


