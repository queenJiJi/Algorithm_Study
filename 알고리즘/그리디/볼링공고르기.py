import sys
from itertools import combinations
sys.stdin = open(
    '/Users/jiyeonpark/Desktop/Python/알고리즘/Algorithm_Study/알고리즘/그리디/input/볼링공고르기.txt', 'r')
n, m = map(int, input().split())  # n: 공의 갯수, m: 공의 무게 종류
balls = list(map(int, input().split()))
answer = 0
result = list(combinations(balls, 2))
# for i in result:
#     if i[0] != i[1]:
#         answer += 1

# print(answer)

# sol2 # 조합라이브러리 없이 풀기
arr = [0]*11
for i in balls:
    arr[i] += 1

for i in range(1, m+1):
    n -= arr[i]
    answer += arr[i] * n
print(answer)
