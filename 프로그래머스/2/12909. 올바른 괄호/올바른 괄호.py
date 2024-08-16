def solution(s):
    stack = []  # 변수명을 stack으로 일관되게 사용
    
    for bracket in s:
        if bracket == "(":  # 비교 연산자를 ==로 수정
            stack.append(bracket)
        elif bracket == ")":  # 비교 연산자를 ==로 수정
            if not stack:
                return False
            stack.pop()
    return not stack  # stack이 비어 있으면 True, 아니면 False
