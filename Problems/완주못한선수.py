from collections import Counter

def solution(participant, completion):
    answer= []
    dic = Counter(participant)
    for k in completion:
        if k in dic:
            dic[k]-=1
    for k in dic:
        if dic[k]>0:
            answer.append(k)
    
    return ''.join(answer) 

print(solution(participant = ["mislav", "stanko", "mislav", "ana"],
completion = ["stanko", "ana", "mislav"]))
