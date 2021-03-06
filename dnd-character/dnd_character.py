# import random
import math
from random import SystemRandom


class Character:
    """
    For a game of Dungeons & Dragons, each player starts
    by generating a character they can play with.

    This character has, among other things, six abilities:
    strength, dexterity, constitution, intelligence, wisdom and charisma.
    """

    # Your character's initial hitpoints are 10
    character_initial_hitpoints = 10

    def __init__(self):

        self.character_constitution_modifier = None
        self.character_hitpoints = None

        self.abilities = {
            'strength': 0,
            'dexterity': 0,
            'constitution': 0,
            'intelligence': 0,
            'wisdom': 0,
            'charisma': 0
        }

        self._set_abilities()
        self._set_character_constitution_modifier()
        self._set_character_hitpoints()

    def _set_character_hitpoints(self):
        self.character_hitpoints = Character.character_initial_hitpoints + \
                                   self.character_constitution_modifier
        return None

    def _set_character_constitution_modifier(self):
        """
        You find your character's constitution modifier by subtracting 10
        from your character's constitution, divide by 2 and round down.

        :return:
        """
        self.character_constitution_modifier = int(math.floor(
            (self.abilities['constitution'] -
             Character.character_initial_hitpoints) / 2))
        return None

    def _set_abilities(self):
        """
        These six abilities have scores that are determined randomly.
        You do this by rolling four 6-sided dice and
        record the sum of the largest three dice.
        You do this six times, once for each ability.

        :return:
        """
        for key in self.abilities.keys():
            self.abilities[key] = roll_dice()
        return None

    @property
    def strength(self):
        return self.abilities['strength']

    @property
    def dexterity(self):
        return self.abilities['dexterity']

    @property
    def constitution(self):
        return self.abilities['constitution']

    @property
    def intelligence(self):
        return self.abilities['intelligence']

    @property
    def wisdom(self):
        return self.abilities['wisdom']

    @property
    def charisma(self):
        return self.abilities['charisma']

    @property
    def hitpoints(self):
        return self.character_hitpoints

    def ability(self):
        """
        Returns random ability
        :return:
        """
        # Standard pseudo-random generators are not
        # suitable for security/cryptographic purposes.
        # random_key_index = random.randint(0, len(self.abilities.keys()) - 1)

        # create a random number that is cryptographically secure
        # Source: https://stackoverflow.com/questions/20936993/
        # how-can-i-create-a-random-number-that-is-cryptographically-secure-in-python
        crypto = SystemRandom()
        random_key_index = crypto.randrange(len(self.abilities.keys()))
        random_key = list(self.abilities.keys())[random_key_index]
        return self.abilities[random_key]


def modifier(constitution: int):
    """
    You find your character's constitution modifier by subtracting 10
    from your character's constitution, divide by 2 and round down.

    :param constitution:
    :return:
    """

    return int(math.floor((constitution -
                           Character.character_initial_hitpoints) / 2))


def roll_dice():
    """
    Rolling four 6-sided dice and record the sum of the largest three.
    :return:
    """

    results = list()
    while len(results) != 4:
        # Standard pseudo-random generators are not
        # suitable for security/cryptographic purposes.
        # results.append(random.randint(1, 6))
        crypto = SystemRandom()
        random_key_index = crypto.randrange(1, 6)
        results.append(random_key_index)

    return sum(sorted(results)[1:])
