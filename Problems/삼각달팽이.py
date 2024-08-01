def solution(n):
    # 2차원 배열 초기화
    tmp = [[0] * i for i in range(1, n + 1)]
    num = 1
    r,c = 0,0
    pos =[[1,0],[0,1],[-1,-1]] # 아래, 오른쪽, 왼쪽 대각선 위
    dir = 0

    while num<=(n*(n+1))//2:
        tmp[r][c] = num
        nr,nc = r+pos[dir][0], c+pos[dir][1]
        
        if nr<0 or nc<0 or nr>=n or nc>=n or tmp[nr][nc]!=0: # 이런 경우
            dir=(dir+1)%3 # 방향전환
            nr,nc = r+pos[dir][0], c+pos[dir][1]
        num+=1
        r,c = nr,nc

    # print(tmp)  
    answer = []
    for t in tmp:
        answer.extend(t)
    return answer
    
print(solution(4))  # [1, 2, 9, 3, 10, 8, 4, 5, 6, 7]
print(solution(5))  # [1, 2, 12, 3, 13, 11, 4, 14, 15, 10, 5, 6, 7, 8, 9]
print(solution(6))

