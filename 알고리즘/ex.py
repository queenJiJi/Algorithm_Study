arr = [0] * 11
n, m = 8, 5  # n: 공의 갯수, 볼링공의 무게 종류
data = [1, 5, 4, 3, 2, 4, 5, 2]
for i in data:
    arr[i] += 1

print(arr)

result = 0

for i in range(1, m+1):
    n -= arr[i]
    result += arr[i] * n  # B가 선택하는 경우의 수와 곱해주기

print(result)
