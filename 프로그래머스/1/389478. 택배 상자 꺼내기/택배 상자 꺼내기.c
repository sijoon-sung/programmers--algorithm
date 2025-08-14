#include <stdio.h>

// 좌표를 상자 번호로 변환하는 도우미 함수
int coord_to_box_num(int r, int c, int w) {
    if (r % 2 == 0) { // 짝수 행 (L -> R)
        return r * w + c + 1;
    } else { // 홀수 행 (R -> L)
        return r * w + (w - 1 - c) + 1;
    }
}

// 반복적 O(n/w) 해법
int solution(int n, int w, int num) {
    if (num > n) return 0; // 예외 처리

    // 1. 목표 상자의 좌표 계산
    int target_row = (num - 1) / w;
    int base_col = (num - 1) % w;
    int target_col;
    if (target_row % 2 == 0) { // 짝수 행
        target_col = base_col;
    } else { // 홀수 행
        target_col = (w - 1) - base_col;
    }

    // 2. 제거할 상자 개수 계산
    int count = 1; // 목표 상자 자신 포함
    int total_rows = (n - 1) / w + 1;

    // 3. 목표 상자 위쪽 행들을 순회
    for (int r = target_row + 1; r < total_rows; ++r) {
        // 현재 행(r), 목표 열(target_col)에 있는 상자 번호 계산
        int box_above = coord_to_box_num(r, target_col, w);
        
        // 해당 상자가 실제로 존재하는지 확인 (n 이하)
        if (box_above <= n) {
            count++;
        }
    }

    return count;
}