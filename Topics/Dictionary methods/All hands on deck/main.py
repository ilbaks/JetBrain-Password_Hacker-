aver_rank = 0
deck_cards ={'2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9', '10': '10', 'Jack': '11',
             'Queen': 12, 'King': 13, 'Ace': 14}
for _ in range(6):
    aver_rank += int(deck_cards.get(input()))
print(aver_rank / 6)
