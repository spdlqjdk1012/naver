# https://www.acmicpc.net/problem/2643
import sys
N = int(input())

# 입력값      [[1, 2], [8, 7], [20, 10], [20, 20], [15, 12], [12, 14], [11, 12]]
# 가로세로정렬 [[1, 2], [7, 8], [10, 20], [20, 20], [12, 15], [12, 14], [11, 12]]
a = [sorted(list(map(int, sys.stdin.readline().split(" ")))) for _ in range(N)]

# a[0] 기준으로 정렬하고 a[0] 값이 동일하면 a[1]기준으로 다시 정렬한다
# [[1, 2], [7, 8], [10, 20], [11, 12], [12, 14], [12, 15], [20, 20]]
a = sorted(a, key=lambda x:(x[0], x[1]))

dp = [0] * N
for idx, val in enumerate(a):
    dp[idx] = 1
    for j in range(idx):
        if val[1] >= a[j][1]: # 세로길이는 이미 정렬이 되어있으니 가로만 보면됨
            dp[idx] = max(dp[j]+1, dp[idx])
print(max(dp))