# 찾기(Find)함수를 최적화하기 위한 방법으로 '경로 압축'을 이용할 수 있음
# 찾기(Find)함수를 재귀적으로 호출한 뒤에 '부모 테이블 값을 바로 갱신'하기

# 모두 그대로인데 아래 부분만 이렇게 바로 찾아서 갱신시키는 방향으로 개선시키면 경로 압축가능
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
  # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]


'''
이전엔,
def find_parent(parent,x):
  if parent[x]!=x:
    return find_parent(parent,parent[x])
  return x
'''


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
