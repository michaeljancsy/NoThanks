"""Strategies: Player methods that call self.take or self.pass_

New strategies for the game can be developed in strategies.py"""

from random import choice


def default_strategy(self, table, players):
    """
    Randomly chooses between take or pass. Chooses take if player has no
    chips. This strategy is assigned to newly instantiated Player objects.
    """
    if self.chips:
        random_play = choice([self.take, self.pass_])
        random_play(table)
    else:
        self.take(table)
