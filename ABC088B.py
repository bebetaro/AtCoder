times = int(input())
cards = input()

cards = cards.split()
for i, card in enumerate(cards):
    cards[i] = int(card)
cards.sort(reverse=True)
# print(cards)

Alice = []
Bob = []

for i, card in enumerate(cards):
    if i % 2 == 0:
        Alice.append(int(card))
    else:
        Bob.append(int(card))

result = sum(Alice) - sum(Bob)

print(result)
