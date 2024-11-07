def backtrack(letters, path, used, results):
    if len(path) == len(letters):
        results.add("".join(path))  # 조건을 만족하는 조합을 저장
        return

    for i in range(len(letters)):
        # 이미 사용한 문자이거나, 이전 문자와 같은 경우를 제외
        if used[i] or (i > 0 and letters[i] == letters[i - 1] and not used[i - 1]):
            continue
        # 백트래킹 조건 설정
        if path and path[-1] == letters[i]:
            continue

        used[i] = True
        path.append(letters[i])
        backtrack(letters, path, used, results)
        path.pop()
        used[i] = False

def solution(letters):
    letters = sorted(letters)  # 사전순 출력을 위해 정렬
    results = set()  # 중복 방지를 위해 set 사용
    backtrack(letters, [], [False] * len(letters), results)
    
    # 출력
    sorted_results = sorted(results)
    return sorted_results

# 테스트
print(solution('abca')  )
print(solution('wxyz')  )




def solution(power, players):
    k=0
    init = power
    while 1:
      gain = 0
      win =True 
      for player in players:
        init = init+k
        if init>power:
            gain+=1
            win=True
        else:
            win=False
      init += int(init-(init-player))*0.1
      if win:
          return k
      else:
          k+=1

print(solution(1,[1,2,3,10000]))
          

    