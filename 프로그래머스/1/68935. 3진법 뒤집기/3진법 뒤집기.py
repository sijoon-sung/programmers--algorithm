def solution(n):
    #3진법을 스택을 활용해서 
    trinary =""
    while n > 0:
        trinary = str(n % 3) + trinary
        n//=3
    
    # 3진법 뒤집기
    reversed_trinary = trinary[::-1]
    
    # 수정된 부분: 3진법 10진법
    decimal = 0
    for i in range(len(trinary)):
        decimal += int(reversed_trinary[i])*(3**(len(reversed_trinary)-i-1))
    return decimal