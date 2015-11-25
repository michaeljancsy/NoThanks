from random import choice


def default(self, table, players):
    if self.chips:
        random_play = choice([self.take, self.pass_])
        random_play(table)
    else:
        self.take(table)


def heuristic(self, table, players):
    # take if the marginal point value is less than 1 + the expected remainder
    # (note that the expected remainder doesn't include others' coins)
    # IN PROGRESS
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
