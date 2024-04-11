import sys
sys.stdin = open(
    '/Users/jiyeonpark/Desktop/Algorithm Notes/알고리즘공부/input/금광.txt', 'r')
'''
아이디어: 
1. arr[i][j] = i행, j열에 존재하는 금의 양
2. dp[i[][j] = i행 j열까지의 최적의 해(얻을 수 있는 금의 최댓값)
3. 점화식: 
    dp[i][j] = arr[i][j](현재금의값) + max(dp[i-1][j-1] , dp[i][j-1], dp[i+1][j-1]
4. 테이블에 접근할때마다 리스트의 범위를 벗어나지 않는지 체크해야함
5. dp 테이블에 바로 초기데이터를 담아서 적용 가능

'''
N = int(input())
answer = 0
for tc in range(N):
    n, m = map(int, input().split())
    board = list(map(int, input().split()))

    # 다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화
    dp = []
    index = 0
    for _ in range(n):
        dp.append(board[index:index+m])
        index += m

    # 다이나믹 프로그래밍 진행
    for c in range(1, m):  # 2번째 열부터 시작 - 각 열마다 확인
        for r in range(n):
            # 왼쪽 위에서 오는 경우
            if r == 0:  # 인덱스 확인
                left_up = 0
            else:
                left_up = dp[r-1][c-1]
            # 왼쪽 아래에서 오는 경우
            if r == n-1:
                left_down = 0
            else:
                left_down = dp[r+1][c-1]
            # 왼족에서 오는 경우
            left = dp[r][c-1]
            dp[r][c] = dp[r][c] + max(left_up, left_down, left)

    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])  # dp의 가장 오른쪽 열에 기억되어있는 값을 가져옴
    print(result)

    print('dp:', dp)

    # for k in range(len(board)//n):
    #     answer+= max(board[k::m])
    # print(answer)
    # answer=0
