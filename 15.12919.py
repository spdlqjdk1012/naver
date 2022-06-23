S = input()
T = input()
flag = False
def change(arr):
    global S
    global flag
    if len(arr) <= len(S):
        if arr == S:
            flag = True
        return
    tmp = list(arr)
    if tmp[-1] == "A":
        tmp.pop(-1)
        change(''.join(s for s in tmp))
    if tmp[0] == "B":
        arr = list(arr)
        arr.pop(0)
        arr = ''.join(s for s in arr)
        change("".join(reversed(arr)))
change(T)
if flag == True:
    print(1)
else:
    print(0)