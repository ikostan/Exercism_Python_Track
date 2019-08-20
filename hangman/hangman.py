# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman(object):
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word = word
        self.masked_word = '_' * len(word)

    def guess(self, char):

        if self.status != STATUS_ONGOING:
            raise ValueError("ERROR: no guesses left")

        if char in self.word and char not in self.masked_word:
            chars = []
            for c in self.word:
                if c == char:
                    chars.append(c)
                else:
                    chars.append('_')
            new_word = ''.join(chars)

            masked = ''
            for i, c in enumerate(new_word):
                if c != '_':
                    masked += c
                else:
                    masked += self.masked_word[i]
            self.masked_word = masked

            if self.masked_word == self.word:
                self.status = STATUS_WIN

        else:
            self.remaining_guesses -= 1

            if self.remaining_guesses < 0:
                self.status = STATUS_LOSE

        print("{} : {}".format(self.masked_word, self.word))

    def get_masked_word(self):
        return self.masked_word

    def get_status(self):
        return self.status
