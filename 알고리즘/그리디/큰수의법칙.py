import sys
sys.stdin = open(
    '/Users/jiyeonpark/Desktop/Python/알고리즘/Algorithm_Study/알고리즘/그리디/input/큰수의법칙.txt', 'r')
n, m, k = map(int, input().split())

arr = list(map(int, input().split()))


def sol(array, M, K):
    answer = 0
    array.sort(reverse=True)
    while M > 0:
        if M < 1:
            return answer
        for _ in range(K):
            if M < 1:
                return answer
            answer += array[0]
            M -= 1
        answer += array[1]
        M -= 1
    return answer


print(sol(arr, m, k))
