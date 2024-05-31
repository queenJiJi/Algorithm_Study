from itertools import permutations

def solution(n,k):

  return ''.join(map(str,list(permutations(range(1,n+1),n))[k-1]))

print(solution(3,3))
print(solution(4,9))
print(solution(3,1))