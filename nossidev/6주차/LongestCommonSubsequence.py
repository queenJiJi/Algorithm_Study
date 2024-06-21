def solution(text1, text2):
    text1_len_lg = len(text1)+1 # out of bound 방지를 위해 하나씩 늘려주기
    text2_len_lg = len(text2)+1

    dp = [[0]* text2_len_lg for _ in range(text1_len_lg)]

    for i in range(1,text1_len_lg):
        for j in range(1,text2_len_lg):
            if text1[i-1] == text2[j-1]: # 각 값이 일치할 경우
                dp[i][j] = dp[i-1][j-1]+1 # 이전 대각선에서 +1 (+1은 한 이유는 해당 부분이 일치했으니까)
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) # 위쪽과 왼쪽에서 값 업데이트
    return dp[i][j] # 최종적으로 가장 오른쪽 아래가 모든 비교를 끝냈을때 최종 업데이트 된 값일 테니까


print(solution('abcde','ace'))
print(solution('abc','abc'))
print(solution('abc','def'))
print(solution('ezupkr','ubmrapg'))
print(solution("bsbininm","jmjkbkjkv"))
print(solution("oxcpqrsvwf","shmtulqrypy"))