def is_same_format(hand: str) -> bool:
    h = hand.split(' ')
    return h[0][-1] == h[1][-1] == h[2][-1] == h[3][-1] == h[4][-1]


def sort_hand(hand: str) -> str:
    decks = hand.split(' ')
    is_sorted = False

    while not is_sorted:
        is_sorted = True
        for i, deck in enumerate(decks):
            if i + 1 < len(decks):
                if DECK_RANK.index(deck[:-1]) > DECK_RANK.index(decks[i + 1][:-1]):
                    is_sorted = False
                    decks[i], decks[i + 1] = decks[i + 1], decks[i]

    return ' '.join(decks)


def is_four_of_a_kind(hand: str) -> bool:
    cards = sort_hand(hand).split(' ')

    if cards[0][:-1] == cards[1][:-1] == cards[2][:-1] == cards[3][:-1]:
        return True

    if cards[1][:-1] == cards[2][:-1] == cards[3][:-1] == cards[4][:-1]:
        return True

    return False


def is_straight(hand) -> bool:
    # print('\nhand: {}'.format(hand))
    sorted_hand = sort_hand(hand).split(' ')
    # print('\nsorted_hand: {}'.format(sorted_hand))

    return (DECK_RANK.index(sorted_hand[0][:-1]) + 1 == DECK_RANK.index(sorted_hand[1][:-1]) or
            (DECK_RANK.index(sorted_hand[0][:-1]) + (len(DECK_RANK) - 1)) == DECK_RANK.index(sorted_hand[4][:-1])) and \
           DECK_RANK.index(sorted_hand[1][:-1]) + 1 == DECK_RANK.index(sorted_hand[2][:-1]) and \
           DECK_RANK.index(sorted_hand[2][:-1]) + 1 == DECK_RANK.index(sorted_hand[3][:-1]) and \
           DECK_RANK.index(sorted_hand[3][:-1]) + 1 == DECK_RANK.index(sorted_hand[4][:-1])


def is_flush(hand: str) -> bool:
    sorted_hand = sort_hand(hand).split(' ')

    if DECK_RANK.index(sorted_hand[0][:-1]) + 1 == DECK_RANK.index(sorted_hand[1][:-1]) and \
            DECK_RANK.index(sorted_hand[1][:-1]) + 1 == DECK_RANK.index(sorted_hand[2][:-1]) and \
            DECK_RANK.index(sorted_hand[2][:-1]) + 1 == DECK_RANK.index(sorted_hand[3][:-1]):
        return True

    if DECK_RANK.index(sorted_hand[1][:-1]) + 1 == DECK_RANK.index(sorted_hand[2][:-1]) and \
            DECK_RANK.index(sorted_hand[2][:-1]) + 1 == DECK_RANK.index(sorted_hand[3][:-1]) and \
            DECK_RANK.index(sorted_hand[3][:-1]) + 1 == DECK_RANK.index(sorted_hand[4][:-1]):
        return True

    return False


def is_full_house(hand: str) -> bool:
    sorted_hand = sort_hand(hand).split(' ')

    if (sorted_hand[0][:-1] == sorted_hand[1][:-1] and
        sorted_hand[1][:-1] == sorted_hand[2][:-1]) and \
            sorted_hand[3][:-1] == sorted_hand[4][:-1]:
        return True

    if sorted_hand[0][:-1] == sorted_hand[1][:-1] and \
            (sorted_hand[2][:-1] == sorted_hand[3][:-1] and
             sorted_hand[3][:-1] == sorted_hand[4][:-1]):
        return True

    return False


def is_three_of_a_kind(hand) -> bool:
    sorted_hand = sort_hand(hand).split(' ')

    if sorted_hand[0][:-1] == sorted_hand[1][:-1] and \
            sorted_hand[1][:-1] == sorted_hand[2][:-1]:
        return True

    if sorted_hand[2][:-1] == sorted_hand[3][:-1] and \
            sorted_hand[3][:-1] == sorted_hand[4][:-1]:
        return True

    if sorted_hand[1][:-1] == sorted_hand[2][:-1] and \
            sorted_hand[2][:-1] == sorted_hand[3][:-1]:
        return True

    return False


def is_two_pair(hand) -> bool:
    sorted_hand = sort_hand(hand).split(' ')
    # print('\nis_two_pair: {}'.format(sorted_hand))

    if sorted_hand[0][:-1] == sorted_hand[1][:-1] and \
            sorted_hand[2][:-1] == sorted_hand[3][:-1]:
        return True

    if sorted_hand[1][:-1] == sorted_hand[2][:-1] and \
            sorted_hand[3][:-1] == sorted_hand[4][:-1]:
        return True

    if sorted_hand[0][:-1] == sorted_hand[1][:-1] and \
            sorted_hand[3][:-1] == sorted_hand[4][:-1]:
        return True

    return False


def is_one_pair(hand) -> bool:
    sorted_hand = sort_hand(hand).split(' ')

    if sorted_hand[0][:-1] == sorted_hand[1][:-1]:
        return True

    if sorted_hand[1][:-1] == sorted_hand[2][:-1]:
        return True

    if sorted_hand[2][:-1] == sorted_hand[3][:-1]:
        return True

    if sorted_hand[3][:-1] == sorted_hand[4][:-1]:
        return True

    return False


def is_high_card(hand) -> bool:
    return True


DECK_RANK = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']

RANK = {
    # 0: 'Five of a kind',
    1: ('Straight flush', is_same_format, is_straight),
    2: ('Four of a kind', is_four_of_a_kind),
    3: ('Full house', is_full_house),
    4: ('Flush', is_same_format, is_flush),
    5: ('Straight', is_straight),
    6: ('Three of a kind', is_three_of_a_kind),
    7: ('Two pair', is_two_pair),
    8: ('One pair', is_one_pair),
    9: ('High card', is_high_card),
}
