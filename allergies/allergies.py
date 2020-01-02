class Allergies:

    def __init__(self, score):

        self._items = {
            1: 'eggs',
            2: 'peanuts',
            4: 'shellfish',
            8: 'strawberries',
            16: 'tomatoes',
            32: 'chocolate',
            64: 'pollen',
            128: 'cats',
        }

        self._score = score % 256

    def allergic_to(self, item):
        return item in self.lst

    @property
    def lst(self):

        allergies = list()
        score = self._score

        for key in sorted(self._items.keys(), reverse=True):

            if score >= key:
                score -= key
                allergies.append(self._items[key])

            if score == 0:
                break

        return allergies



