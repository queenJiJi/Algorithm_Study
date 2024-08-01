def solution(phone_book):
  pb= sorted(phone_book)

  for i in range(len(pb)-1):
    if pb[i+1].startswith(pb[i]):
      return False
  return True

print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))