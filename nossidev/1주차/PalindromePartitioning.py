# def partition(s):
#     if not s:
#         return []
#     lists = []
#     partitions = []

#     def backtrack(start):
#         if start == len(s):
#             lists.append(partitions[:])
#             return
#         for i in range(start + 1, len(s) + 1):
#             tmp_str = s[start:i]
#             if tmp_str == tmp_str[::-1]:
#                 partitions.append(tmp_str)
#                 backtrack(i)
#                 partitions.pop()

#     backtrack(0)
#     return lists
    
  
# print(partition(s='aab'))
  

# def solution(s):
#   result =[]
#   part = []

#   if not s: return []

#   def backtrack(start):
#     # base case
#     if start == len(s):
#       result.append(part[:])
#       return
  
#     for i in range(start+1, len(s)+1):
#       partition = s[start:i]

#       if partition == partition[::-1]: # palindrome이라면
#         part.append(partition)
#         backtrack(i)
#         part.pop()
#   backtrack(0)         
#   return result


# print(solution(s='aab'))



def solution(s):
  result = []
  part =[]

  def backtrack(start):
    if start == len(s):
      result.append(part.copy())
      return
    for i in range(start,len(s)):
      if isPalindrome(s,start,i):
        part.append(s[start:i+1]) 
        backtrack(i+1)
        part.pop()

  backtrack(0)

  return result

def isPalindrome(s,left,right):
  while left<right:
    if s[left] != s[right]:
      return False
    left = left+1
    right = right-1
  return True

print(solution(s='aab'))