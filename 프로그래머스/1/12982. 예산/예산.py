def solution(d, budget):
    answer = 0 
    d.sort()
    result = 0
    for num in d:
        result += num
        answer += 1
        if result > budget:
            answer -= 1
            break
    return answer
