def solution(n, arr):
    stack = []
    answer = [-1] * n
    
    for i in range(n):
        while stack and arr[stack[-1]] < arr[i]:
            answer[stack.pop()] = arr[i]
        stack.append(i)    
    return answer

print(solution(4, [3, 5 ,2 ,7]))
print(solution(4,[9,5,4,8]))

