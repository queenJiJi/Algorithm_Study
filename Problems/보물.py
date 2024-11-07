# def solution(A,B):
#   s=0
#   A.sort()
#   new_B= B

#   for i in range(len(A)):
#     s+= (new_B[new_B.index(max(new_B))]*A[i])
#     new_B.remove(max(new_B))
#   return s



# print(solution([1, 1, 1, 6, 0],[2, 7, 8, 3, 1]))
# print(solution([1, 1, 3],[10,30,20]))
# print(solution([5, 15, 100, 31, 39, 0, 0, 3, 26],[11, 12, 13, 2, 3, 4, 5, 9, 1]))

n = input()
A = list(map(int,input().split()))
B = list(map(int, input().split()))
print(n,A,B)