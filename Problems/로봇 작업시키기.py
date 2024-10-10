def solution(sizes, limits,tasks):
  result = []

  for idx, val in enumerate(tasks):
    if len(val)-1 <= 0:
      work = int(val[0]) * 1
    else:
      work = int(val[0])*sizes[idx]**(len(val)-1)
    if work<=limits[idx]:
      result.append(1)
    else:
      result.append(0)

  return result


print(solution([10, 2, 13, 1],[300, 31, 100, 5],['3tt', '4ttt', '8t', '4tttt']))
print(solution([100, 100, 100], [1000000000, 100, 3],["9tttt", "1t", "4"]))