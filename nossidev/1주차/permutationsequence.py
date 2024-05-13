from itertools import permutations

def solution(n,k):
  # sol1
  return ''.join(map(str, list(permutations(range(1,n+1),n))[k-1]))

  # sol2 => 실패
  # arr = [i for i in range(1,n+1)]
  # length = len(arr)
  # answer=''
  # recur_num = k

  # def factorial(n):
  #   if n==1:
  #     return 1
  #   return n*factorial(n-1)
  
  # for i in range(n):
  #   pop_idx= (recur_num)//factorial(n-1-i)+1
  #   recur_num = (recur_num)%factorial(n-1-i)
  #   if arr==[]:
  #     break
  #   answer+=str(arr.pop(pop_idx))
    
  # return answer



print(solution(n=3,k=3))
print(solution(n=4,k=9))
print(solution(n=3,k=1))
