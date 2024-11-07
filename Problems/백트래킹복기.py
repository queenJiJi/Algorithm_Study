def solution(letters):
  result = set()
  used = [False] * len(letters)
  
  def backtrack(cur):
    if len(cur) == len(letters):
      result.add(cur)
      return

    for i in range(len(letters)):

      if (i>0 and letters[i-1] == letters[i]) or used[i]:
        continue
      
      if cur and cur[-1] == letters[i]:
        continue 

      used[i]= True
      backtrack(cur+letters[i])
      used[i] = False

  backtrack('')
  results = sorted(result)
  return results


 
print(solution("abca")) # Output: ['abca', 'acab', 'acba', 'baca', 'bcaa', 'cbaa']
print(solution("xyzk"))




