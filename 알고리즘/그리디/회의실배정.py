n = int(input())
meetings = [list(map(int,input().split())) for _ in range(n)]
meetings.sort(key= lambda x:x[1])
end = 0
answer = 0

# print(meetings)
for s,e in meetings:
    
    if s >= end:
        answer+=1
        end = e
print(answer)

