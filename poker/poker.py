from hand import Hand


# TODO
def best_hands(hands: list) -> list:
    max_rank = 9  # lowest rank by default
    hands_objects = list()
    for hand in hands:
        obj = Hand(hand)
        # filter out lowest ranks based
        # on updated max_rank value (optimization)
        if max_rank >= obj.rank_key:
            max_rank = obj.rank_key
            hands_objects.append(obj)

    # filter out lowest ranks from the list
    is_filtered = False
    while not is_filtered:
        is_filtered = True
        for i, hand in enumerate(hands_objects):

            # Filter out by rank
            if hand.rank_key > max_rank:
                is_filtered = False
                del hands_objects[i]
                break

            # compare objects between themselves
            if i + 1 < len(hands_objects):

                if hand < hands_objects[i + 1]:
                    is_filtered = False
                    del hands_objects[i]
                    break

                if hand > hands_objects[i + 1]:
                    is_filtered = False
                    del hands_objects[i + 1]
                    break

    # return list of hands
    return [h.hand for h in hands_objects]
