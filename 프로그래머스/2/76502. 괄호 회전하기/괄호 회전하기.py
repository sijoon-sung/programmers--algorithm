def solution(s):
    answer = 0
    n = len(s)
    
    for i in range(n):
        stack = []
        for j in range(n):
            c = s[(i + j) % n]  # 회전 문자열을 사용
            
            if c in "({[":
                stack.append(c)
            else:
                if not stack:
                    break
                if c == ")" and stack[-1] == "(":
                    stack.pop()
                elif c == "}" and stack[-1] == "{":
                    stack.pop()
                elif c == "]" and stack[-1] == "[":
                    stack.pop()
                else:
                    break
        else:
            if not stack:  # 모든 괄호가 닫혔으면
                answer += 1
                
    return answer
