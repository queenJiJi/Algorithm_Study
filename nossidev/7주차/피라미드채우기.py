def solution(blocks):
    
    board = [[0]*(i+1) for i in range(len(blocks))] # 피라미드를 넣어줄 빈 이중배열 만들어주기 
    
    for floor, (pos, val) in enumerate(blocks):
        board[floor][pos] = val # board에 맞는 위치에 값들 채워넣어주기  
        
        left, right = pos, pos # 기준점 = 값이 있는 위
        # 기준점으로부터 왼쪽 채워나가기 
        while left>0:
            board[floor][left-1] = board[floor-1][left-1] - board[floor][left]
            left-=1
        # 지준점으로부터 오른쪽 채워나가기    
        while right<floor:
            board[floor][right+1] = board[floor-1][right] - board[floor][right]
            right+=1
    # 값들만 arr에 넣어서 출력해주기 
    answer = []
    for ans in board:
        answer+=ans

    return answer


print(solution([[0, 50], [0, 22], [2, 10], [1, 4], [4, -13]]))
print(solution([[0, 92], [1, 20], [2, 11], [1, -81], [3, 98]]))