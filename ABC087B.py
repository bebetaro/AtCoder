five_h = int(input())
one_h = int(input())
fif_t = int(input())
price = int(input())

five_h += 1
one_h += 1
fif_t += 1

counter = 0

for i in range(five_h):
    for j in range(one_h):
        for k in range(fif_t):
            result = 500*i + 100*j + k*50
            if result == price:
                counter += 1
print(counter)
