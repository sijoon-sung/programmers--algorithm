def solution(numbers):
    answer = set() #최종합에서 반복되는 숫자를 없애기 위해서 사용
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.add(numbers[i] + numbers[j]) #완전 탐색 구조로 2개의 배열을 순회하면서 더함
    return sorted(answer)
