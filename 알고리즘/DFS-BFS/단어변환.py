from collections import deque

# 두 단어가 한 글자만 다른지 확인하는 함수
def is_okay(word1,word2):
    diff_cnt = sum(1 for x,y in zip(word1,word2) if x!=y)
    if diff_cnt > 1:
        return False
    return True
    
def solution(begin,target,words):

    if target not in words:
        return 0
    
    q = deque()
    q.append((begin,0)) # 현재 단어, 변환횟수
    visited =set() # 방문한 단어 트래킹

    while q:
        current_word, cnt = q.popleft()

        if current_word == target:
            return cnt 
        
        # 아직 방문하지 않은 단어 중 변환 가능한 단어 탐색
        for word in words:
            if word not in visited and is_okay(current_word,word):
                visited.add(word) # 방문처리
                q.append((word,cnt+1))
    return 0 # 변환할 수 없는 경우