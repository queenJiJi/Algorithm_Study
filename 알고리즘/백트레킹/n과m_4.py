n,s = map(int, input().split())
arr= list(map(int, input().split()))
cnt = 0
tmp =[]
def backtrack(start):
    global cnt

    if tmp and sum(tmp) == s:
        cnt += 1

    for idx in range(start,n):
        tmp.append(arr[idx])
        backtrack(idx+1)  
        tmp.pop()

backtrack(0)

print(cnt)