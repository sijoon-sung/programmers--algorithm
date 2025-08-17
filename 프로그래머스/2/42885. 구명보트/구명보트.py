def solution(people, limit):
    # greedy - 하나의 부분 문제를 만들어야 함
    people.sort()
    
    
    answer = 0
    left = 0
    right = len(people) - 1
    
    while (left <= right):
        answer += 1
        
        if(people[right] + people[left] <= limit):
            left += 1
        
        right -= 1
    
    
    return answer
