import sys
n, w, L = map(int, input().split())
truck = list(map(int, input().split()))
cnt = 0
bridge = []
time = []
while True:
    for i in range(len(bridge)):
        time[i] += 1
    for _ in range(len(bridge)):
        if time[0] > w:
            bridge.pop(0)
            time.pop(0)
        else:
            break
    if len(truck) == 0 and len(bridge) == 0:
        print(cnt+1)
        sys.exit()
    if len(truck) != 0:
        if sum(bridge) + truck[0] <= L and len(bridge) < w:
            bridge.append(truck.pop(0))
            time.append(1)
            stand = 1
    cnt += 1