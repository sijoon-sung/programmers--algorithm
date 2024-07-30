def solution(array):
    # 가장 큰 숫자에 맞게 리스트 크기 설정
    number = [0 for i in range(max(array) + 1)]
    
    # 숫자의 빈도수를 세기
    for num in array:
        number[num] += 1
    
    # 최빈값 찾기
    max_count = max(number)
    answer = [i for i, count in enumerate(number) if count == max_count]
    if len(answer) > 1:
        answer = -1
    else:
        answer = answer.pop()
    return answer