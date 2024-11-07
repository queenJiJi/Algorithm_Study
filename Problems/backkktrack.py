def backtrack(letters, tmp, visited,result):
  if len(letters) == len(tmp):
    result.add(''.join(tmp))
    return
  
  for i in range(len(letters)):
    if visited[i] or (i>0 and letters[i]==letters[i-1] and not visited[i-1]):
      continue

    if tmp and tmp[-1]==letters[i]:
      continue
    
    visited[i] = True
    tmp.append(letters[i])
    backtrack(letters,tmp,visited,result)
    tmp.pop()
    visited[i]= False

def solution(letters):

  letters= sorted(letters)
  result = set()

  backtrack(letters, [], [False]* len(letters), result)
 
    
  return [val for val in sorted(result)]


print(solution('abca'))
print(solution('xyzk'))