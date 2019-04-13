numbers = input().split()
x = input().split()
y = input().split()
z = input().split()

k = int(numbers[3])

answer = []
for i in x:
    for j in y:
        price = int(i)+int(j)
        answer.append(price)
answer.sort(reverse=True)
del answer[k::]
f_ans = []
for m in answer:
    for n in z:
        price = m + int(n)
        f_ans.append(price)

f_ans.sort(reverse=True)
del f_ans[k::]

for l in f_ans:
    print(l)
