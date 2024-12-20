'''
# 서로소 집합은 '무방향 그래프 내에서의 사이클을 판별'할 때 사용할 수있음
  # 참고로 방향 그래프에서의 사이클 여부는 DFS이용해서 판별 가능

# 사이클 판별 알고리즘:
  1. 각 간선을 하나씩 확인하며 두 노드의 루트노드를 확인(Find함수 호출)
    1) 루트노드가 서로 다르다면 두 노드에 대하여 합집합 연산을 수행(같은 집합으로 만들기)
    2) 루트노드가 서로 같다면 사이클이 발생한 것
  2. 그래프에 포함되어 있는 모든 간선에 대하여 1번 과정을 반복 
  -> 2번을 했는데도 사이클이 없다면, 해당 그래프에는 사이클이 없다고 판별
'''
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

cycle = False  # 사이클 발생 여부

for i in range(e):
    a, b = map(int, input().split())
    # 사이클이 발생한 경우 종료
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    # 사이클이 발생하지 않았다면(같은 집합에 없다면 같은 집합이 될 수 있게) 합집합 수행해보기
    else:
        union_parent(parent, a, b)

if cycle:
    print("사이클이 발생했습니다.")
else:
    print("사이클이 발생하지 않았습니다.")
