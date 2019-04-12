times = int(input())
time = 0
x = 0
y = 0
result = "OK"

for i in range(times):
    move = input()
    move = move.split()
    time = int(move[0]) - time
    x_diff = int(move[1]) - x
    y_diff = int(move[2]) - y
    distance = x_diff + y_diff
    possibility = time - distance
    if possibility >= 0 and possibility % 2 == 0:
        x = int(move[1])
        y = int(move[2])
        time = int(move[0])
    else:
        result = "NG"

if result == "OK":
    print("Yes")
else:
    print("No")
