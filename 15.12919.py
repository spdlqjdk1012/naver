S = input()
T = input()
flag = False
def change(arr):
    global T
    global flag
    if len(arr) >= len(T):
        if arr == T:
            flag = True
        return
    tmp = arr + "A"
    change(tmp)
    arr = arr + "B"
    change("".join(reversed(arr)))
change(S)
if flag == True:
    print(1)
else:
    print(0)