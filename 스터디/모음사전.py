# from itertools import product

# def solution(word):
#   ch = ['A','E','I','O','U']
#   cases =[]
#   for i in range(1,len(ch)+1):
#     for case in product(ch, repeat=i):
#         cases.append(''.join(case))

#   cases.sort()
#   return cases.index(word)+1

def solution(word):
  ch=['A','E','I','O','U']
  answer = []

  def backtrack(cur_word):

    if len(cur_word) > 5:
      return 
    
    if cur_word:
      print(cur_word)
      answer.append(cur_word)
    
    for c in ch:
      backtrack(cur_word+c)

  backtrack('')
  return answer.index(word)+1

print(solution('AAAAE'))
print(solution('AAAE'))
print(solution('I'))
print(solution('EIO'))