import sys
N, M= map(int, input().split())
bucket = []
result_list = [0] * (N+1)
for i in range(M):
    bucket.append(list(map(int, input().split())))
for ball in bucket:
    for i in range(ball[0], ball[1] + 1):
        result_list[i] = ball[2]
for i in range(1, len(result_list)):
    print(result_list[i])