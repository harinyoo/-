###시간초과###
# import sys
#
# T = int(sys.stdin.readline())
# for t in range(T):
#     K = int(sys.stdin.readline())
#     cost = [0] + list(map(int, sys.stdin.readline().split()))
#     for i in range(1, K+1):
#         cost[i] += cost[i-1]
#
#     dp = [[0]*(K+1) for _ in range(K+1)]
#     for i in range(2, K+1):
#         for j in range(1, K-i+2):
#             dp[j][j+i-1] = min([dp[j][j+k]+dp[j+k+1][j+i-1] for k in range(i-1)]) + cost[j+i-1] - cost[j-1]
#     print(dp[1][K])


# import sys
# case = int(sys.stdin.readline())
# for i in range(case):
#     n = int(sys.stdin.readline())
#     ch = list(map(int,sys.stdin.readline().split()))
#     # D선언
#     D = [[0 for i in range(n)] for i in range(n)]
#     A = [[0 for i in range(n)] for i in range(n)]
#     #초기화
#     for i in range(n-1):
#         D[i][i+1] = ch[i]+ ch[i+1]
#         A[i][i+1] = i+1
#     #본격적인 연산
#     for dig in range(2, n):
#         for i in range(n-dig):
#             j = i + dig
#             min = 100000000
#             for k in range(A[i][j-1], A[i+1][j]+1):
#                 tmp = D[i][k-1] + D[k][j]
#                 if min > tmp:
#                     min = tmp
#                     A[i][j] = k
#             D[i][j] = min  + sum(ch[i:j+1])
#     print(D[0][n-1])



import sys


n = int(input())

while n > 0:
    n -= 1
    K = int(input())
    file_list = list(map(int, sys.stdin.readline().split()))
    dp = [[0 for _ in range(K)] for _ in range(K)]
    sum = [0] * (K + 1)  # 첫번째부터 K번짹 까지의 파일크기합 한번 합칠때 추가비용
    sum[1] = file_list[0]
    for i in range(1, K + 1):  # i번째 파일까지의 합
        sum[i] = sum[i - 1] + file_list[i - 1]

    knuth = [[0 for _ in range(K)] for _ in range(K)]  # Knuth's Optimization 각 구간에서 나오는 k 저장
    for i in range(K):  # 초기화화
        knuth[i][i] = i

    for x in range(1, K):  # x만큼 더한 구간의 구하기
        for i in range(K - x):  # 시작위치 i에서 i+x까지 구간 잡아주기
            j = i + x
            dp[i][j] = 999999999999
            for k in range(knuth[i][j - 1], knuth[i + 1][j] + 1):  # 범위에 knuh 최적화를 적용
                if k < K - 1 and dp[i][j] > dp[i][k] + dp[k + 1][j] + sum[j + 1] - sum[i]:  # 최솟값찾기
                    dp[i][j] = dp[i][k] + dp[k + 1][j] + sum[j + 1] - sum[i]
                    knuth[i][j] = k

    print(dp[0][K - 1])
