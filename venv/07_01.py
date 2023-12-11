from collections import Counter
from functools import cmp_to_key

ans = 0
cards = []
cards_order = '23456789TJQKA'

with open("07.data.txt") as file:
    for line in file:
        if line:
            hand, bid = line.split()
            cards.append((hand, int(bid)))

def cmp_cards(a: tuple[str, int], b: tuple[str, int]) -> int:
    for hand1, hand2 in zip(a[0], b[0]):
        if cards_order.index(hand1) > cards_order.index(hand2):
            return 1
        elif cards_order.index(hand1) < cards_order.index(hand2):
            return -1
    return 0

def hand_to_value(hand:str()) -> int:
    hand = Counter(hand)
    hand_len = len(hand)
    if hand_len == 1:               #AAAAA
        return 7
    if hand_len == 2:
        if 4 in hand.values():      #AAAAK
            return 6
        return 5                    #AAAKK
    if hand_len == 3:
        if 3 in hand.values():      #AAAKQ
            return 4
        return 3                    #AAKKQ
    if hand_len == 4:               #AAKQJ
        return 2
    return 1                        #AKQJT

def cmp_hands(a: tuple[str, int], b: tuple[str, int]) -> int:
    return hand_to_value(a[0]) - hand_to_value(b[0])

cards.sort(key=cmp_to_key(cmp_cards))
cards.sort(key=cmp_to_key(cmp_hands))

print(cards)

for idx, card in enumerate(cards, 1):
    ans += idx * card[1]

print(ans)