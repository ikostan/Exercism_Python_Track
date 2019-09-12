def find_anagrams(word, candidates):
    """
    Given a word and a list of possible anagrams, select the correct sublist.

    EXAMPLE:
    Given "listen" and a list of candidates like "enlists" "google" "inlets" "banana"
    the program should return a list containing "inlets".
    :param word:
    :param candidates:
    :return:
    """

    # create a sorted chars list:
    sorted_word = sorted([w.lower() for w in word])

    # return the results
    return [candidate for candidate in candidates if is_anagram(word, sorted_word, candidate)]


def is_anagram(word, sorted_word, candidate):
    """
    Compare between two strings and return True in case <candidate> is anagram of <word>.
    Otherwise return False.
    :param word:
    :param sorted_word:
    :param candidate:
    :return:
    """

    # filter identical words:
    if word.lower() != candidate.lower():
        # compare between sorted char lists:
        if sorted_word == sorted([w.lower() for w in candidate]):
            return True
    return False
