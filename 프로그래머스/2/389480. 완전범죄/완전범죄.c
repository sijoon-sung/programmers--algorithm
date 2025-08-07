#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
#define MAX 120

int solution(int** info, size_t info_rows, size_t info_cols, int n, int m) {
    bool dp[MAX][MAX] = {{false}};
    dp[0][0] = true; // 초기 상태 설정

    for (int k = 0; k < info_rows; k++) {
        int a_trace = info[k][0];
        int b_trace = info[k][1];
        bool next_dp[MAX][MAX] = {{false}}; // 다음 상태 배열 초기화

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (!dp[i][j]) continue;

                // A가 물건을 훔치는 경우 (누적 혼적 < n)
                if (i + a_trace < n) {
                    next_dp[i + a_trace][j] = true;
                }
                // B가 물건을 훔치는 경우 (누적 혼적 < m)
                if (j + b_trace < m) {
                    next_dp[i][j + b_trace] = true;
                }
            }
        }
        memcpy(dp, next_dp, sizeof(dp)); // 상태 업데이트
    }

    // 최소 A 혼적 탐색
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (dp[i][j]) {
                return i;
            }
        }
    }
    return -1; // 가능한 상태 없음
}