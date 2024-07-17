import sys
answer=0
N = int(input())
standard = sys.stdin.readline()
words = [sys.stdin.readline() for _ in range(N-1)]

for word in words:
    word= list(word)
    copy_st= list(standard)
    for w in word[:]:
        if w in copy_st:
            word.remove(w)
            copy_st.remove(w)
    if len(copy_st)<=1 and len(word)<=1:
        answer+=1
print(answer)