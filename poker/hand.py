from helper_methods import DECK_RANK, RANK, get_total_hand_rank, sort_hand


class Hand:
    """
    Standard 52-card deck
    Source: https://en.wikipedia.org/wiki/Standard_52-card_deck
    List of poker hands:
    Source: https://en.wikipedia.org/wiki/List_of_poker_hands
    """

    def __init__(self, hand: str):
        self.__hand: str = hand
        self.__sorted_hand: list = sort_hand(hand).split(' ')
        self.__rank: str = self.__get_rank()
        self.__rank__key: int = self.__get_rank_key()

    def get_triplet_pair(self) -> tuple:
        if self.rank_key == 3:
            if self.sorted_hand[0][:-1] == self.sorted_hand[2][:-1]:
                return self.sorted_hand[0:3], self.sorted_hand[3:]
            return self.sorted_hand[2:], self.sorted_hand[:2]
        raise Exception('This method available for \'Full house\' only!')

    @property
    def quadruplet_card(self) -> str:
        if self.sorted_hand[0][:-1] == self.sorted_hand[3][:-1]:
            return self.sorted_hand[0]
        return self.sorted_hand[-1]

    def get_one_pair(self) -> list:
        if self.__rank == 'One pair':
            if self.sorted_hand[0][:-1] == self.sorted_hand[1][:-1]:
                return self.sorted_hand[:2]
            elif self.sorted_hand[1][:-1] == self.sorted_hand[2][:-1]:
                return [self.sorted_hand[1], self.sorted_hand[2]]
            elif self.sorted_hand[2][:-1] == self.sorted_hand[3][:-1]:
                return [self.sorted_hand[2], self.sorted_hand[3]]
            elif self.sorted_hand[3][:-1] == self.sorted_hand[4][:-1]:
                return [self.sorted_hand[3], self.sorted_hand[4]]
        raise Exception('This method available for \'One pair\' only!')

    def get_two_pairs(self) -> list:
        if self.__rank == 'Two pair':
            pairs = [card for card in self.sorted_hand if card != self.kicker]
            print('pairs: {}'.format(pairs))
            return pairs
        raise Exception('This method available for \'Two pair\' only!')

    # TODO: rewrite so that it will fit: Three of a kind, One pair
    @property
    def kicker(self) -> str:
        if self.__rank == 'Four of a kind':
            if self.sorted_hand[0][:-1] == self.sorted_hand[3][:-1]:
                return self.sorted_hand[-1]
            return self.sorted_hand[0]
        elif self.__rank == 'Two pair':
            if self.sorted_hand[0][:-1] == self.sorted_hand[1][:-1] and \
                    self.sorted_hand[3][:-1] == self.sorted_hand[4][:-1]:
                return self.sorted_hand[2]
            elif self.sorted_hand[0][:-1] == self.sorted_hand[1][:-1] and \
                    self.sorted_hand[2][:-1] == self.sorted_hand[3][:-1]:
                return self.sorted_hand[4]
            else:
                return self.sorted_hand[0]
        elif self.__rank == 'One pair':
            if self.sorted_hand[0][:-1] == self.sorted_hand[1][:-1]:
                return ''.join(self.sorted_hand[2:])
            elif self.sorted_hand[1][:-1] == self.sorted_hand[2][:-1]:
                return ''.join(self.sorted_hand[0] + self.sorted_hand[3:])
            elif self.sorted_hand[2][:-1] == self.sorted_hand[3][:-1]:
                return ''.join(self.sorted_hand[0:2] + [self.sorted_hand[4]])
            elif self.sorted_hand[3][:-1] == self.sorted_hand[4][:-1]:
                return ''.join(self.sorted_hand[:3])

        raise Exception('There is no kicker for {}'.format(self.__rank))

    @property
    def sorted_hand(self):
        return self.__sorted_hand

    @property
    def highest_card_key(self) -> int:
        # baby straight
        if self.rank_key == 5 and \
                self.sorted_hand[-1][:-1] == '2' and \
                self.sorted_hand[0][:-1] == 'A':
            return DECK_RANK.index(self.__sorted_hand[1][:-1])
        return DECK_RANK.index(self.__sorted_hand[0][:-1])

    @property
    def hand(self) -> str:
        return self.__hand

    @property
    def rank(self) -> str:
        return self.__rank

    @property
    def rank_key(self) -> int:
        return self.__rank__key

    # TODO
    def __lt__(self, other):
        print('ls')
        # x<y calls x.__lt__(y)
        return not self.__gt__(other) and not self.__eq__(other)

    # TODO
    def __gt__(self, other):
        print('gt')
        # x>y calls x.__gt__(y)
        if self.rank_key < other.rank_key:
            return True

        if self.rank_key == other.rank_key:
            # Straight flush, Straight
            if self.rank_key in [1, 5]:
                return self.highest_card_key < other.highest_card_key
            # Four of a kind
            elif self.rank_key == 2:
                if DECK_RANK.index(self.quadruplet_card[:-1]) < DECK_RANK.index(other.quadruplet_card[:-1]):
                    return True
                elif DECK_RANK.index(self.quadruplet_card[:-1]) == DECK_RANK.index(other.quadruplet_card[:-1]):
                    if DECK_RANK.index(self.kicker[:-1]) < DECK_RANK.index(other.kicker[:-1]):
                        return True
                return False
            # Full house
            elif self.rank_key == 3:
                # print('Full house: gt')
                triplet, pair = self.get_triplet_pair()
                other_triplet, other_pair = other.get_triplet_pair()
                if DECK_RANK.index(triplet[0][:-1]) < DECK_RANK.index(other_triplet[0][:-1]):
                    return True
                elif DECK_RANK.index(triplet[0][:-1]) == DECK_RANK.index(other_triplet[0][:-1]):
                    if DECK_RANK.index(pair[0][:-1]) < DECK_RANK.index(other_pair[0][:-1]):
                        return True
                return False
            # Two pair
            elif self.rank_key == 7:
                # Each two pair is ranked first by the rank
                # of its highest-ranking pair, then by the rank
                # of its lowest-ranking pair, and finally by
                # the rank of its kicker.
                for pair in zip(self.get_two_pairs(), other.get_two_pairs()):
                    if DECK_RANK.index(pair[0][:-1]) < DECK_RANK.index(pair[1][:-1]):
                        return True
                    elif DECK_RANK.index(pair[0][:-1]) > DECK_RANK.index(pair[1][:-1]):
                        return False
                if DECK_RANK.index(self.kicker[:-1]) < DECK_RANK.index(other.kicker[:-1]):
                    return True
                return False
            # One pair
            elif self.rank_key == 8:

                if self.get_one_pair()[0][:-1] > other.get_one_pair()[0][:-1]:
                    return False

                for pair in zip(self.kicker.split(' '), other.kicker.split(' ')):
                    if pair[0][:-1] > pair[1][:-1]:
                        return False

                return True
            # High Card, Flush, Three of a kind
            elif self.rank_key in [4, 6, 9]:
                for pair in zip(self.sorted_hand, other.sorted_hand):
                    print('\npair: {}'.format(pair))
                    if DECK_RANK.index(pair[0][:-1]) < DECK_RANK.index(pair[1][:-1]):
                        return True
                    elif DECK_RANK.index(pair[0][:-1]) > DECK_RANK.index(pair[1][:-1]):
                        return False
                return False

        return False

    # TODO
    def __eq__(self, other):
        print('eq')
        # x==y calls x.__eq__(y)
        if not isinstance(other, Hand):
            # don't attempt to compare against unrelated types
            return NotImplemented

        if self.rank_key == other.rank_key:
            # Straight flush is ranked by the
            # rank of its highest-ranking card.
            # Straight flush, Straight
            if self.rank_key in [1, 5]:
                return self.highest_card_key == other.highest_card_key
            # Four of a kind
            elif self.rank_key == 2:
                # Each four of a kind is ranked first by the rank of its
                # quadruplet, and then by the rank of its kicker.
                if DECK_RANK.index(self.quadruplet_card[:-1]) == DECK_RANK.index(other.quadruplet_card[:-1]):
                    if DECK_RANK.index(self.kicker[:-1]) == DECK_RANK.index(other.kicker[:-1]):
                        return True
                return False
            # Full house
            elif self.rank_key == 3:
                # Each full house is ranked first by the rank of its triplet,
                # and then by the rank of its pair.
                # print('Full house: eq')
                triplet, pair = self.get_triplet_pair()
                other_triplet, other_pair = other.get_triplet_pair()
                if DECK_RANK.index(triplet[0][:-1]) == DECK_RANK.index(other_triplet[0][:-1]) and \
                        DECK_RANK.index(pair[0][:-1]) == DECK_RANK.index(other_pair[0][:-1]):
                    return True
                return False
            # Two pair
            elif self.rank_key == 7:
                # Each two pair is ranked first by the rank of its highest-ranking pair,
                # then by the rank of its lowest-ranking pair, and finally by the rank
                # of its kicker.
                for pair in zip(self.get_two_pairs(), other.get_two_pairs()):
                    if DECK_RANK.index(pair[0][:-1]) != DECK_RANK.index(pair[1][:-1]):
                        return False
                if DECK_RANK.index(self.kicker[:-1]) != DECK_RANK.index(other.kicker[:-1]):
                    return False
                return True
            # One pair
            elif self.rank_key == 8:
                # Each one pair is ranked first by the rank of its pair,
                # then by the rank of its highest-ranking kicker, then by
                # the rank of its second highest-ranking kicker, and finally
                # by the rank of its lowest-ranking kicker.
                if self.get_one_pair()[0][:-1] != other.get_one_pair()[0][:-1]:
                    return False

                for pair in zip(self.kicker.split(' '), other.kicker.split(' ')):
                    if pair[0][:-1] != pair[1][:-1]:
                        return False

                return True
            elif self.rank_key in [4, 6, 9]:
                print('High Card, Flush')
                # Each high card hand is ranked first by the rank of its
                # highest-ranking card, then by the rank of its second highest-ranking
                # card, then by the rank of its third highest-ranking card, then by
                # the rank of its fourth highest-ranking card, and finally by the rank
                # of its lowest-ranking card.
                results = list()
                for pair in zip(self.sorted_hand, other.sorted_hand):
                    results.append(DECK_RANK.index(pair[0][:-1]) == DECK_RANK.index(pair[1][:-1]))
                print('eq [4,6,9] -> results: {}'.format(results))
                return all(results)

            return True

        return False

    def __get_rank_key(self) -> int:
        for key, value in RANK.items():
            if value[0] == self.rank:
                return key

    def __get_rank(self) -> str:
        for key in sorted(RANK.keys()):
            # print('\nKEY: {}'.format(key))
            results = list()
            for func in RANK[key][1:]:
                results.append(func(self.hand))

            if all(results):
                print('\nRANK: {}, HAND: {}'.format(RANK[key][0], self.hand))
                return RANK[key][0]

    def __repr__(self):
        return '{}'.format(self.sorted_hand)
