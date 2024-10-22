n,m = map(int, input().split())
answer = []
def backtrack(tmp):
    
    if m == len(tmp):
        answer.append(tmp[:])
        return
        
    for i in range(1,n+1):
        if i not in tmp:
            tmp.append(i)
            backtrack(tmp)
            tmp.pop()
backtrack([])

for val in answer:
    print(*val)
        
#1 2
#1 3
#1 4
#2 1
#2 3
#2 4
#3 1
#3 2
#3 4
#4 1
#4 2
#4 3
    
    
    
    