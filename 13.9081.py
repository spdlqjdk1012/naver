T = int(input())
for _ in range(T):
    arr = list(input())
    flag = False
    for i in range(1, len(arr)):
        if arr[-i] > arr[-i-1]:
            tmp = i
            flag = True
            break
    if flag == False:
        print("".join(arr))
        continue
    minimum = max(arr)
    for j in range(tmp-1, len(arr)):
        if arr[j] > arr[-tmp-1]:
            minimum = min(minimum, arr[j])
            minum = j
    arr[-tmp-1], arr[minum] = arr[minum], arr[-tmp-1]
    tmpsort = sorted(arr[-tmp:])
    result = arr[0:-tmp]+tmpsort
    print("".join(result))

# T = int(input())
# def dfs(depth):
#     global flag
#     global tmp
#     if depth == len(arr):
#         if tmp == arr:
#             result.append(tmp)
#             overlap = tmp
#             flag = True
#         elif flag == True:
#             result.append(tmp)
#         return
#     overlap = ""
#     for i in range(len(brr)):
#         if vis[i] == True or brr[i] == overlap:
#             continue
#         vis[i] = True
#         overlap = brr[i]
#         bmp = tmp
#         tmp += brr[i]
#         dfs(depth+1)
#         if len(result) == 2:
#             return
#         tmp = bmp
#         vis[i] = False
# for _ in range(T):
#     arr = input()
#     brr = sorted(arr)
#     vis = [False]*len(brr)
#     result = []
#     tmp = ""
#     flag = False
#     dfs(0)
#     if len(result) == 2:
#         print(result[1])
#     else:
#         print(arr)