def solution(seoul):
    index = 0
    for i in seoul:
        if i == "Kim":
            break
        index += 1
    answer = '김서방은 ' + str(index) + '에 있다'
    return answer