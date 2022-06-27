import sys
N = int(input())
paper = []
for _ in range(N):
    tmp = sorted(list(map(int, input().split())))
    paper.append(tmp)
paper = sorted(paper, key=lambda x:(x[0], x[1]))
vis = [1]*N
for index, value in enumerate(paper):
    for i in range(index):
        if value[1] >= paper[i][1]:
            vis[index] = max(vis[i]+1, vis[index])
print(max(vis))