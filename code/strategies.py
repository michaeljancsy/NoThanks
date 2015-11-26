"""Strategies: functions that call take or pass_"""

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


def heuristic(self, table, players):
    """
    Simple strategy, still in development. Roughly, it takes a card if the
    card's value is less than the average value of card's remaining on the
    table, adjusting for the number of included chips.
    """
    # take if the marginal point value is less than 1 + the expected remainder
    cards_in_hands = set()
    for player in players.list_:
        cards_in_hands.update(player.hand)
    remaining_cards = set(table.cards) - cards_in_hands
    mean_remaining_card_value = \
        sum(remaining_cards) / len(remaining_cards) - table.chips
    if table.card <= mean_remaining_card_value or self.chips == 0:
        self.take(table)
    else:
        self.pass_(table)
