# from itertools import permutations
# def solution(numbers):
#   answer =0
#   for x in list(permutations(numbers)):
#     answer=max(answer,int(''.join(map(str, x))))
#   return str(answer)


def solution(numbers):
  nums = list(map(str, numbers))
  nums.sort(key=lambda x: x*2, reverse=True)
  return ''.join(nums)

print(solution([6,10,2]))
print(solution([3,30,34,5,9]))