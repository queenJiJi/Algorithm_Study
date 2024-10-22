n,m = map(int, input().split())
arr = list(map(int, input().split()))
answer = []
def backtrack(tmp):

    if len(tmp) == m:
        answer.append(tmp[:]) 
        return

    for i in arr:
        if i not in tmp:
            tmp.append(i)
            backtrack(tmp)
            tmp.pop()

backtrack([])

answer.sort()
for i in answer:
    print(*i)