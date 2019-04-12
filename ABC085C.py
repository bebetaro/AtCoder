otoshidama = input()
otoshidama = otoshidama.split()
cash = int(otoshidama[0])
price = int(otoshidama[1])

#print(cash, price)

answer = []


for i in range(cash+1):
    for j in range(cash+1-i):
        k = cash - i-j
        result = 10000*i + 5000*j + 1000 * k
        if result == price:
            answer.append(str(i)+" "+str(j)+" "+str(k))

if len(answer) > 0:
    print(answer[0])
else:
    print("-1 -1 -1")
