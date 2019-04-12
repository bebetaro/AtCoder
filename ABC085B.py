times = int(input())
mochis = []

for i in range(times):
    mochi = int(input())
    mochis.append(mochi)

mochis = list(set(mochis))

print(len(mochis))
