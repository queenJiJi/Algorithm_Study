import sys
sys.stdin = open(
    '/Users/jiyeonpark/Desktop/Python/알고리즘/Algorithm_Study/알고리즘/그리디/input/숫자카드게임.txt', 'r')
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# answer = []

# for i in range(n):
#     answer.append(min(arr[i]))

# print(max(answer))


# sol 2)
answer = 0
for i in range(n):
    min_val = min(arr[i])  # 현재 줄에서 가장 작은 수 찾기
    answer = max(answer, min_val)  # 작은 수 들 중에 가장 큰 수 찾기

print(answer)
