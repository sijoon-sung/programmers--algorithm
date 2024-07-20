def solution(dots):
    def slope(n,k):
        return (dots[n-1][0] - dots[k-1][0]) / (dots[n-1][1] - dots[k-1][1])
         
    if slope(1,2) == slope (3,4):
        return 1
    elif slope(1,3) == slope(2,4):
        return 1
    elif slope(2,3) == slope(1,4):
        return 1
    return 0
