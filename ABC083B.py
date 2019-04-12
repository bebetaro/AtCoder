numbers = input()

numbers = numbers.split()

counter = 0
for i in range(int(numbers[0])):
    i += 1
    tmp = 0
    if i > 9:
        for j in str(i):
            tmp += int(j)
    else:
        tmp = i

    if int(numbers[1]) <= tmp <= int(numbers[2]):
        counter += i

print(counter)
