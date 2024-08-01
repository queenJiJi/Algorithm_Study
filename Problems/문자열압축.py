s = input()
n = len(s)
answer= ''
cnt = 1
for i in range(1,n):
    if s[i-1]==s[i]:
        cnt+=1
    else:
        answer+=(s[i-1]+str(cnt))
        cnt =1
answer+=(s[-1]+str(cnt))
print(answer)
