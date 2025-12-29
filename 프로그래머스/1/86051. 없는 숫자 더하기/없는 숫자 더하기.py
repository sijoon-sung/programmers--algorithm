def solution(numbers):
    list_number = list(range(0,10))
    
    for i in numbers:
        if(i in list_number):
            list_number.remove(i)
    
    answer = sum(list_number)
    return answer