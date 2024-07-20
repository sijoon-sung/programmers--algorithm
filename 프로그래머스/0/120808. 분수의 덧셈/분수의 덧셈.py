def solution(numer1, denom1, numer2, denom2):
    n = denom1 * denom2
    k =numer1 * denom2
    j = numer2*denom1
    div = k + j
    for num in range(n, -1, -1):
        if div % num ==0 and n % num ==0:
            answer = [div //num , n //num]
            return answer
