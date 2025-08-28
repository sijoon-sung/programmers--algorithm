def solution(s):
    index = 0
    # list_s 변수는 불필요하므로 제거했습니다.
    answer = []
    
    # len(s) > index 라고 쓰는 것이 더 일반적입니다.
    while(len(s) > index):
        letter = s[index]
        found_match = False # 일치하는 문자를 찾았는지 확인하는 '깃발' 역할

        # 가장 가까운 것을 찾아야 하므로, 현재 위치 바로 앞에서부터 거꾸로 탐색합니다.
        # range(시작, 끝, 간격) -> range(index-1 부터, 0 까지, -1씩 감소)
        for i in range(index - 1, -1, -1):
            if(letter == s[i]):
                # 일치하는 문자를 찾았을 때
                distance = index - i  # 현재 위치와 찾은 위치의 거리를 계산
                answer.append(distance)
                found_match = True  # 찾았다고 표시
                break  # 가장 가까운 하나만 찾으면 되므로 더 이상 탐색할 필요 없음
        
        # for 루프가 끝날 때까지 문자를 찾지 못했다면
        if not found_match:
            answer.append(-1)
            
        index += 1
    
    return answer