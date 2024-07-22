def solution(dirs):
    def is_valid_move(nx, ny):
        return 0 <= nx < 11 and 0 <= ny < 11
    
    def location(x, y, dir):
        if dir == "U":
            nx, ny = x, y + 1
        elif dir == "D":
            nx, ny = x, y - 1
        elif dir == "R":
            nx, ny = x + 1, y
        elif dir == "L":
            nx, ny = x - 1, y
        return nx, ny
    
    movement = set()  # 안겹치게 set로 선언
    x, y = 5, 5  # 초기 좌표를 (5, 5)로 설정 (0,0) -> (5,5)로 바꿔야지 0<= x,y < 11 범위 내에서 작업할 수 있음)
    
    for dir in dirs:
        nx, ny = location(x, y, dir)
        if is_valid_move(nx, ny):
            # 움직인 경로와 반대 경로를 모두 저장
            movement.add((x, y, nx, ny))
            movement.add((nx, ny, x, y))
            x, y = nx, ny  # 좌표 갱신
    
    return len(movement) // 2  # 이동한 경로의 개수는 양방향으로 저장되었으므로 2로 나눔

# 테스트
print(solution("ULURRDLLU"))  # 예상 결과: 7
print(solution("LULLLLLLU"))  # 예상 결과: 7
