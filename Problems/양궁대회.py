from itertools import combinations_with_replacement
def solution(n, info):
    answer = []
    max_diff = 0
    for arr in combinations_with_replacement(range(11),n):
        target = [0]*11
        for j in arr:
            target[j]+=1
        a = 0
        r = 0
        for k in range(11):
            if target[k]!=0 or info[k]!=0:
                if info[k]>=target[k]:
                    a+=(10-k)
                else:
                    r+=(10-k)
        if r>a:
            diff = r-a
            if diff>=max_diff:
                # answer = []
                answer.append((diff,target[::-1]))
                max_diff = diff
            
    answer.sort(key=lambda x:(x[0],x[1]), reverse=True)
    
    if not answer:
        return [-1]
    return answer[0][::-1]            
    

# print(solution(5,[2,1,1,1,0,0,0,0,0,0,0]))
print(solution(9,[0,0,1,2,0,1,1,1,1,1,1]))
