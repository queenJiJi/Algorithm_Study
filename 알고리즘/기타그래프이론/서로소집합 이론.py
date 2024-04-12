'''
서로소 집합 = 공통 원소가 없는 두  집합 
ex) {1,2},{3,4} 는 서로소 관계이다
    {1,2},{2,3}은 서로소 관계가 아니다

[ 서로소 집합 자료구조 ]
'서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조' 
* 서로소 집합 자료구조는 두 종류의 연산을 지원:
  # 합집합(Union) : 두개의 원소가 포함된 집합을 하나의 집합으로 합치는 연산
  # 찾기(Find) : 특정한 원소가 속한 집합이 어떤 집합인지 알려주는 연산
# 서로소 집합 자료구조는 '합치기 찾기(Union Find)' 자료구조 라고 불리기도 함

< 여러개의 합치기 연산이 주어졌을 때 서로소 집합 자료구조의 동작과정 > 
1. 합집합(Union)연산을 확인하여, 서로 연결된 두 노드 A,B를 확인
  1) A와 B의 루트노드 A',B'를 각각 찾는다
  2) A'를 B'의 부모 노드로 설정 
2. 모든 합집합(Union)연산을 처리할 때까지 1번 과정을 반복 
'''

# [ 기본적인 서로소 집합 알고리즘 ]

# 특정원소가 속한 집합을 찾기


def find_parent(parent, x):
    # 루트 노드가 아니라면 ,루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

# 두 원소가 속한 집합을 합치기


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a  # 루트로 거슬러 올라가야하니까 작은 곳으로 올라감
    else:
        parent[a] = b


# 노드의 개수(v)와 간선(union 연산)(e)의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v+1)  # 각 노드의 부모 정보를 적은 테이블 초기화

# 부모 테이블 상에서, 부모를 일단 모두 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합 ', end=' ')
for i in range(1, v+1):
    print(find_parent(parent, i), end=' ')

print()

# 부모 테이블 내용 출력
print('부모테이블: ', end=' ')
for i in range(1, v+1):
    print(parent[i], end=' ')
print()

'''
단, 서로소 집합 자료구조: 기본적인 구현 방법의 문제점
# 합집합연산이 편향되게 이루어지는 경우 찾기(Find) 함수가 비효율적으로 동작함
# 최악의 경우에는 찾기(Find)함수가 '모든 노드를' 다 확인하게 되어 시간복잡도가 O(V)이다.
  # 예를들어, {1,2,3,4,5}의 총 5개의 원소가 존재하는 상황에서
  # 수행된 연산들: Union(4,5),Union(3,4),Union(2,3),Union(1,2)라면,
  5의 부모노트를 찾기위해 5의 부모인 4, 4의 부모인 3, 3의 부모인 2, 2의 부모인 1까지 쭈욱 모든 노드를 탐색해야함
  
  노드번호: 1 2 3 4 5
  부모   : 1 1 2 3 4

  => 이는 수행 시간에서 매우 비효울적임
'''
