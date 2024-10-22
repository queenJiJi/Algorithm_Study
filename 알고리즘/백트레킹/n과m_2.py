n,m = map(int, input().split())
answer = []
def backtrack(start, tmp):
    
    if m == len(tmp):
        answer.append(tmp[:])
        return
        
    for i in range(start,n+1):
        if i not in tmp:
            tmp.append(i)
            backtrack(i+1,tmp)
            tmp.pop()
backtrack(1,[])

for val in answer:
    print(*val)


#1 2
#1 3
#1 4
#2 3
#2 4
#3 4
        
    
    
    
    
    