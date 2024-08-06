def solution(a, b, n):
    cola = n
    result = 0

    while cola >= a:
        gained_cola = (cola // a) * b  # 교환으로 얻는 콜라 수
        result += gained_cola           # 결과에 추가
        cola = gained_cola + (cola % a) # 남은 콜라와 교환 후 얻은 콜라를 합침

    return result
