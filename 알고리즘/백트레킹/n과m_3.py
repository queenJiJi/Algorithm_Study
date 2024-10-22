n,m = map(int, input().split())
answer = []
def backtrack(start, tmp):
    
    if m == len(tmp):
        answer.append(tmp[:])
        return
        
    for i in range(start,n+1):
        tmp.append(i)
        backtrack(i,tmp)
        tmp.pop()
backtrack(1,[])

for val in answer:
    print(*val)