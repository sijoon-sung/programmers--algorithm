def solution(s, n):
    answer = ''
    
    for i in s:
        if i == ' ':  # 공백인 경우
            answer += ' '  # 공백을 그대로 추가
            continue
        elif ord(i) == 90:  # 대문자 Z인 경우
            new_word = 65 + (n - 1)  # Z 다음에 A로 돌아가도록
        elif ord(i) == 122:  # 소문자 z인 경우
            new_word = 97 + (n - 1)  # z 다음에 a로 돌아가도록
        else:
            new_word = ord(i) + n
        
        # 알파벳이 범위를 초과할 경우
        if (i.isupper() and new_word > 90) or (i.islower() and new_word > 122):
            new_word -= 26
        
        answer += chr(new_word)
    
    return answer
