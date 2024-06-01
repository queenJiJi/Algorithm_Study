def longestValidParentheses(s):
        stack = [-1]
        n = len(s)
        answer = 0
        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    answer = max(answer,i-stack[-1])
                else:
                    stack.append(i)
        return answer
