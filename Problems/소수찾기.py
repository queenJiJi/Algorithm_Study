from itertools import permutations
def find(number):
  number = int(number)
  answer= 0
  for i in range(2,number):
    if number % i == 0:
      break
  else:
    answer= number
  return answer

def solution(numbers):
  n = len(numbers)
  answer= 0
  for i in range(1,n+1):
    # for ch in set(''.join(x) for x in permutations(numbers, i)):
    for ch in [''.join(x) for x in permutations(numbers, i)]:
      if ch == '0' or ch == '1' or ch.startswith('0'): continue
      else:
        val =find(ch)
        if val != 0:
          answer+=1
  return answer

print(solution('17'))
print(solution('011'))
