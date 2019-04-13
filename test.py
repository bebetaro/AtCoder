w_length = int(input())
h_length = int(input())

answer = []

t_length = w_length + h_length


def saiki(index, trial):
    if index > 8:
        index = 0
        return saiki(index, trial)
    if trial[index] == 1:
        return saiki(index+1, trial)
    else:
        trial[index] = 1


for i in range(w_length):
    trial = []
    for j in range(t_length):
        trial.append(0)


print(answer)
