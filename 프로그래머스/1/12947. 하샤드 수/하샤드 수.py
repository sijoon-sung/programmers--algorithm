def solution(x):
    # x가 두 자리 이상의 정수인지 확인
    if x < 10:
        return True

    # 각 숫자의 자릿수를 더하기
    digit_sum = sum(int(digit) for digit in str(x))

    # digit_sum이 0인지 확인하여 나누기 오류 방지
    if digit_sum == 0:
        return False

    # x가 digit_sum으로 나누어 떨어지는지 확인
    return x % digit_sum == 0
