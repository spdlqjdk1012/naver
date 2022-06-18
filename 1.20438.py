# N, K, Q, M = map(int, input().split())
# sleepy = list(map(int, input().split()))
# coded = list(map(int, input().split()))
# section = []
# for _ in range(M):
#     section.append(list(map(int, input().split())))
# attend = [False]*N
# for i in range(Q):
#     if coded[i] in sleepy:
#         continue
#     attend[coded[i]-3] = True
#     for j in range(N):
#         if j+3 not in sleepy and coded[i] < j+3 and (j+3)%coded[i] != 0:
#             attend[j] = True
# for i in section:
#     cnt = 0
#     for j in range(i[0], i[1]+1):
#         if attend[j-3] == False:
#             cnt += 1
#     print(cnt)

N, K, Q, M = map(int, input().split())
sleepy = list(map(int, input().split()))
coded = list(map(int, input().split()))
section = []
for _ in range(M):
    section.append(list(map(int, input().split())))
attend = [False]*N
for i in range(Q):
    if coded[i] in sleepy:
        continue
    attend[coded[i]-3] = True
    for j in range(N):
        if j+3 in sleepy:
            continue
        if coded[i] > j+3:
            continue
        else:
            if (j+3)%coded[i] != 0:
                continue
        attend[j] = True
for i in section:
    cnt = 0
    for j in range(i[0], i[1]+1):
        if attend[j-3] == False:
            cnt += 1
    print(cnt)