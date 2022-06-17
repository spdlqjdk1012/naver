# N = int(input())
# A = list(map(int, input().split()))
# vis = [False]*N
# op = list(map(int, input().split()))
# opvis = [0]*4
# number = []
# maximum = 0
# minimum = 0
# result = 0
# def operator(depth):
#     global result
#     result = number[0]
#     if depth == N-1:
#         return
#     for i in range(4):
#         if opvis[i] == op[i]:
#             continue
#         opvis[i] += 1
#         if i == 0:
#             result += number[depth+1]
#             operator(depth+1)
#             result -= number[depth+1]
#             opvis[i] -= 1
#         elif i == 1:
#             result -= number[depth+1]
#             operator(depth+1)
#             result += number[depth+1]
#             opvis[i] -= 1
#         elif i == 2:
#             newresult = result
#             result *= number[depth+1]
#             operator(depth+1)
#             result = newresult
#             opvis[i] -= 1            
#         elif i == 3:
#             newresult = result
#             result = int(result/number[depth+1])
#             operator(depth+1)
#             result = newresult
#             opvis[i] -= 1
# def dfs(depth):
#     global result
#     global maximum
#     global minimum
#     if depth == N:
#         operator(0)
#         if result > maximum:
#             maximum = result
#         elif result < minimum:
#             minimum = result
#         result = 0
#         return
#     for i in range(len(A)):
#         if vis[i]:
#             continue
#         vis[i] = True
#         number.append(A[i])
#         dfs(depth+1)
#         number.pop()
#         vis[i] = False
# dfs(0)
# print(maximum)
# print(minimum)