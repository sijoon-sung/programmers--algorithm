def solution(n):
    a , b = 0, 1
    for _ in range(n):
        a, b = b, (a + b) % (1234567)  # 각 단계에서 MOD로 나눈 나머지를 계산
    return a
