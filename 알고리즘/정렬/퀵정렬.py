# 퀵 정렬: '기준 데이터를 설정'하고 그 '기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법'
# 일반적인 상황에서 가장 많이 사용되는 정렬 알고리즘 중 하나
# 병합 정렬과 더불어 대부분의 프로그래밍 언어의 정렬 라이브러리의 근간이 되는 알고리즘임
# 가장 기본적인 퀵 정릴은 '첫번째 데이터를 기준데이터(Pivot)로 설정함'
# 즉, 가장 첫번째 원소를 pivot 값으로 두고
# 두번째부터끝까지(->) 이 피봇값보다 큰값을 찾고, 동시에
# 마지막부터pivot값전까지(<-) 피봇값보다 작은 값을 찾는다
# 그리고 그 찾은 피봇값보다 큰 값과 피봇값보다 작은 값을 바꿔준다
# 그리고 이것을 계속 반복하다가
# 어느순간 -> <- 가다가 엇갈리는 순간이 나올텐데,
# 그럼 그 순간엔 '피봇'과 '작은데이터'의 위치를 서로 변경한다
# 그리고 피벗을 기준으로 데이터 묶음을 나눈다(:분할, divide)
# 그리고 방금까지 해온 작업을 (피봇을 기준으로) 분할된 양 그룹에 반복해준다(재귀)
# 이때 피봇을 기준으로 왼쪽 집단은 피봇보다 작은값, 오른쪽 집단은 피봇보다 큰 집단 일 것


# 퀵 정렬의 시간 복잡도: O(NlogN)
# 분할된 집단을 기준으로 재귀,재귀니까-> 너비X높이 = N*logN = NlogN
# 하지만 최악의 경우 O(N^2)의 시간 복잡도를 가짐

arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

# VER 1


def quick_sort(arr, start, end):
    if start >= end:  # 원소가 1개인 경우 종료
        return
    pivot = start  # 피봇은 첫번째 원소
    left = start+1
    right = end

    while (left <= right):  # 엇갈리지 않을때까지 반복
        # 피봇보다 큰 데이터를 찾을때까지 반복
        while (left <= end and arr[left] <= arr[pivot]):
            left += 1
        # 피봇보다 작은 데이터를 찾을때까지 반복
        while (right > start and arr[right] >= arr[pivot]):
            right -= 1
        if (left > right):  # 엇렸다면
            arr[right], arr[pivot] = arr[pivot], arr[right]  # 작은 데이터와 피벗을 교체
        else:  # 엇갈리지 않았다면 작은데이터와 큰 데이터를 교체
            arr[left], arr[right] = arr[right], arr[left]

    # 분할 이후 왼쪽 부분과오른쪽 부분에서 각각 정렬 수행
    quick_sort(arr, start, right-1)
    quick_sort(arr, right+1, end)


quick_sort(arr, 0, len(arr)-1)
print(arr)

# VER 2 : 간결하게!


def quick_sort_short(arr):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(arr) <= 1:
        return arr
    pivot = arr[0]  # 피벗은 첫번째 원소
    tail = arr[1:]  # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot]  # 분할된 왼쪽 부분(피봇보다 작은 값들 모임)
    right_side = [x for x in tail if x > pivot]  # 분할 된 오른쪽 부분(피봇보다 큰 값들 모임)

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행하고 ,전체 리스트 반환
    return quick_sort_short(left_side)+[pivot] + quick_sort_short(right_side)


print(quick_sort_short(arr))
