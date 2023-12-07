from collections import Counter

card_order = {"T": "A", "J": "B", "Q": "C", "K": "D", "A": "E"}

def calc_strength(hand):
        freq = list(Counter(hand).values())
        if 5 in freq:
            return 6
        if 4 in freq:
            return 5
        if 3 in freq:
            if 2 in freq:
                return 4
            return 3
        if freq.count(2) == 2:
            return 2
        if 2 in freq:
            return 1
        return 0

with open("input_07.txt", "r") as f:
    lines = f.read().splitlines()

    packed_lines = [line.split() for line in lines]

    hands = []

    for hand, bid in packed_lines:
        hands.append((calc_strength(hand), [card_order.get(c, c) for c in hand], int(bid)))

    hands.sort()

    s = sum([(i + 1) * hand[2] for i, hand in enumerate(hands)])

    print(s)