def solution(n):
    answer = set()
    limit = 10**12 # 정답이 10^12 이하인 경우만 입력으로 주어진다했으니까

    for i in range(1,n+10): # n+10인 이유는 그 근처 값들을 곱했을때 가능한 적당한 큰 수
        val = 1
        for j in range(i,n+10):
            val*=j
            if val>limit: # 곱한 값이 limit을 넘으면 끝내기
                break
            if j>i: # 새로운 더 큰 수가 나올 때 마다
                answer.add(val)
    answer =sorted(answer)
    return answer[n-1]


# 예시 테스트
print(solution(1))
print(solution(2))
print(solution(4))
print(solution(9))
