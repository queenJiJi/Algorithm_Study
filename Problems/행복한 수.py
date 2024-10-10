from functools import reduce
def solution(n):
  cnt = 0
  already = set()
  while 1:
    if n == 1:
      return cnt
    arr = [int(i) for i in str(n)]
    n = reduce(lambda start,val: start+ val**2 , arr, 0 )
    if n in already:
      return -1
    already.add(n)
    cnt+=1

print(solution(19))
print(solution(21))
