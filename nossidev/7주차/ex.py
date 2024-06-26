def solution(n, escalator):
    # DP 테이블 초기화: 큰 값으로 초기화
    dp = [[float('inf')] * 3 for _ in range(n)]
    
    # 첫 행 초기화
    if escalator[0][1] == 0:
        dp[0][1] = 0  # 시작 위치
    if escalator[0][0] == 0:
        dp[0][0] = 1
    if escalator[0][2] == 0:
        dp[0][2] = 1

    # DP 테이블 채우기
    for i in range(1, n):
        for j in range(3):
            if escalator[i][j] == 0:
                if escalator[i-1][j] == 0:
                    dp[i][j] = min(dp[i][j], dp[i-1][j])
                if j > 0 and escalator[i-1][j-1] == 0:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1] + 1)
                if j < 2 and escalator[i-1][j+1] == 0:
                    dp[i][j] = min(dp[i][j], dp[i-1][j+1] + 1)
    return dp
    # 마지막 행의 최소값 반환
    return min(dp[-1])

# 예제 테스트
print(solution(8, [[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 0], [0, 1, 0], [0, 1, 1], [0, 0, 0], [0, 0, 1]]))  # 예상 답: 3
print(solution(4, [[0, 1, 0], [1, 0, 1], [1, 0, 1], [0, 0, 1]]))  # 예상 답: 2
print(solution(5, [[1, 0, 1], [0, 0, 0], [0, 0, 0], [1, 0, 0], [1, 1, 0]]))  # 예상 답: 1