import sys  
input = sys.stdin.readline 
t= int(input().rstrip())  

for _ in range(t):
    n = int(input())
    scores = [list(map(int, input().split())) for _ in range(n)]
    scores.sort()
    pick = 1
    s2 = scores[0][1]
    for i in range(1,n):
        if scores[i][1] < s2:
            pick+=1
            s2 = scores[i][1]
    print(pick)