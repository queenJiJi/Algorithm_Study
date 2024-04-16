# N개의 동전을 이용하여 만들수 없는 양의 정수 금액 중 최솟값 구하라
from itertools import product, permutations, combinations
import sys
sys.stdin = open(
    '/Users/jiyeonpark/Desktop/Python/알고리즘/Algorithm_Study/알고리즘/그리디/input/만들수없는금액.txt', 'r')
n = int(input())  # n: 동전개수
arr = list(map(int, input().split()))
compare = [i for i in range(1, 1000)]
answer = []
for i in range(1, n+1):
    for x in list(permutations(arr, i)):
        answer.append(sum(x))
    # answer.append(result)

for i in compare:
    if i not in set(answer):
        print(i)
        break
