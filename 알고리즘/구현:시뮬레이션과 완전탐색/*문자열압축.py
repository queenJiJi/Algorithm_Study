'''
아이디어: 완전탐색과 같은 느낌으로,
문자열을 1개부터 글자길이 만큼 각각 짤라보면서
중복된 규칙이 있는지 보고, 각각 끝나는 지점에서 압축한 문제열의 길이를 저장
-> 마지막에 그중 최소값 출력
'''


def solution(s):
    result = []

    if len(s) == 1:
        return 1

    for i in range(1, len(s)):
        pre = s[:i]
        count = 1
        answer = ''
        for j in range(i, len(s)+i, i):
            now = s[j: i+j]
            if pre == now:  # 이전 문자열과 같을 경우
                count += 1
            else:  # 이전 문자열과 일치 하지 않는 경우
                if count != 1:  # 중복된 것이 없을 경우
                    answer = answer + str(count) + pre

                else:
                    answer = answer+pre
                pre = now
                count = 1
        result.append(len(answer))
    return min(result)


print(solution('aabbaccc'))
print(solution('ababcdcdababcdcd'))
print(solution('abcabcdede'))
print(solution('abcabcabcabcdededededede'))
print(solution('xababcdcdababcdcd'))
