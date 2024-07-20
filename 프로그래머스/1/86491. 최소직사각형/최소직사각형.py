def solution(sizes):
    max_size =[]
    min_size =[]
    for s in sizes:
        max_size.append(max(s))
        min_size.append(min(s))
    answer = max(max_size) * max(min_size)
    return answer