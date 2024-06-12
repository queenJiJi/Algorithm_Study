import collections
def solution(strs):
  dic = collections.defaultdict(list)

  for s in strs:
    # dic[str(sorted(s))].append(s)
    dic[''.join(sorted(s))].append(s)

  print(dic)
  return dic.values()


print(solution(["eat","tea","tan","ate","nat","bat"]))
print(solution([""]))
print(solution(["a"]))