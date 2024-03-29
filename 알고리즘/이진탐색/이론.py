# 이진탐색 알고리즘
# 순차탐색: 리스트 안에 있는 특정한 '데이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인하는 방법'
# 이진탐색: 정렬되어 있는 리스트에서 '탐색 범위를 절반씩 좁혀가며 데이터를 탐색' 하는 방법
# 이진 탐색은 시작점, 끝점, 중간점을 이용하여 탐색 범위를 설정

# 동작 방식 (이미 배열이 오름차순 정렬되어있는 상태)
# step1: 시작점:0(인덱스임), 끝점:9 중간점 :4 (중간점이 2개일땐 소숫점 제거)
# step2: 그 중간점이 우리가 찾고자하는 값보다 작을 경우, 중간점 이후의 값들은 다 볼 필요 없으므로
# 끝점을 중간점 바로 앞으로 옮기고, 거기서의 중간점을 다시 설정
# step3: 재설정된 중간점(인덱스)의 값이 우리가 찾고자하는 원소보다 작을 경우
# 시작점을 중간점의 바로 다음으로 옮기고, 거기서 시작점이 중간점과 일치할 경우, 우리가 원하는 원소를  찾아냄

# 단계마다 탐색 범위를 2로 나누는 것과 동일하므로 연산횟누는 'LogN에 비례'
#   ex) 초기 데이터의 개수가 32개 일때, 이상적으로 1단계를 거치면 16개의 데이터만 남응ㅁ
#       2단계를 거치면 8개가량의 데이터만 남고-> 3단계를 거치면 4개 가량의 데이터만 남음
# 다시 말해, 이진탐색은 탐색 범위를 절반씩 줄이며,
# 이진탐색의 시간복잡도는: O(logN)을 보장

##################################################################

# 이진탐색 (재귀적 구현)
def binary_search(arr, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    # 찾은 경우 중간점 인덱스를 반환
    if arr[mid] == target:
        return mid
    # 중간점의 값보다 찾고자하는 값이 작은 경우 왼쪽 확인
    elif arr[mid] > target:
        # end값이 중간값바로 이전으로 이동(왼쪽만 보면되니까)
        return binary_search(arr, target, start, mid-1)
    # 중간점의 값보다 찾고자하는 값이 큰 경우 오른쪽 확인
    elif arr[mid] < target:
        # start값이 중간값바로 다음으로 이동(오른쪽만 보면되니까)
        return binary_search(arr, target, mid+1, end)


# n(원소의 갯수)과 target(찾고자하는 값)을 입력받기
n, target = list(map(int, input().split()))

# 전체 원소 입력받기
arr = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(arr, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다")
else:
    print(result+1)


##################################################################

# 이진탐색 (반복문 구현)
def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start+end)//2
        # 찾은 경우 중간점 인덱스를 반환
        if arr[mid] == target:
            return mid
        # 중간점의 값보다 찾고자하는 값이 작은 경우 왼쪽 확인
        elif arr[mid] > target:
            # end값이 중간값바로 이전으로 이동(왼쪽만 보면되니까)
            end = mid-1
        # 중간점의 값보다 찾고자하는 값이 큰 경우 오른쪽 확인
        elif arr[mid] < target:
            # start값이 중간값바로 다음으로 이동(오른쪽만 보면되니까)
            start = mid+1
    return None


# n(원소의 갯수)과 target(찾고자하는 값)을 입력받기
n, target = list(map(int, input().split()))

# 전체 원소 입력받기
arr = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(arr, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다")
else:
    print(result+1)
