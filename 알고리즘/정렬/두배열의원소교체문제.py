# 핵심 아이디어: 매번 배열 A에서 가장 작은 원소를 골라서, 배열 B에서 가장 큰 원소와 교체한다
# 따라서 가장먼저 A오름차순정렬, B 내림차순 정렬한다
# 이후에 두 배열의 원소를 첫번째 인덱스부터 차례로 확인하면서 A원소가 B원소보다 작을때만 교체를 수행한다
# 이 문제에서는 두 배열의 원소가 최대 100,000개까지 입력될 수 있으므로,
# 최악의 경우 O(NlogN)을 보장하는 정렬알고리즘을 이용해야한다.

n, k = map(int, input().split())

arr1, arr2 = [list(map(int, input().split())) for _ in range(2)]

arr1.sort()
arr2.sort(reverse=True)

for i in range(k):
    if arr1[i] < arr2[i]:  # arr1의 원소가 arr2의 원소보다 작을때만 실행
        arr1[i], arr2[i] = arr2[i], arr1[i]
    else:  # arr1의 원소가 arr2보다 크거나 같을때, 반복문을 탈출
        break  # break하면 아예 반복문에서 나가기, continue는 해당 반복 숫자만 차감되고 반복문 이어가기

print(sum(arr1))
