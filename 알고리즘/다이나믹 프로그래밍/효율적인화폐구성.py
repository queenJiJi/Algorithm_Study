n, m = map(int, input().split())

coin_val = [int(input()) for _ in range(n)]

d = [10001] * (m+1)

d[0] = 0
for i in range(n):  # 화폐단위
    for j in range(coin_val[i], m+1):  # 가격
        if d[j-coin_val[i]] != 10001:  # 입력받은 화폐단위로 가격을 만들어낼 수 있다면
            d[j] = min(d[j], d[j-coin_val[i]]+1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])
