import math
n = input()
trans = []
for i in range(5):
    r = int(input())
    trans.append(r)

timer = math.ceil(int(n)/min(trans))+4

print(timer)
