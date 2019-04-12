times = input()
numbers = input()

numbers = numbers.split()
stepper = 0
while True:
    counter = 0
    for i, number in enumerate(numbers):
        number = int(number)
        if number % 2 == 0:
            number = number/2
            counter += 1
            numbers[i] = number
    if counter == int(times):
        stepper += 1
    else:
        break

print(stepper)
