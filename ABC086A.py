number = input()
number = number.split()

result = int(number[0]) * int(number[1])

if result % 2 == 0:
    print("Even")
else:
    print("Odd")
