from itertools import cycle
from random import sample, choice


class Player(object):
    def __init__(self):
        self.hand = set()
        self.chips = 11

    play = None

    def take(self, table):
        # take chips
        self.chips += table.chips
        table.chips = 0
        # take card
        self.hand.add(table.card)
        table.card = table.cards.pop()

    def pass_(self, table):
        self.chips -= 1
        table.chips += 1

    def score(self):
        hand = sorted(self.hand)
        score = -self.chips
        index = 0
        while index < len(hand):
            if index == 0 or hand[index-1] != hand[index]-1:
                score += hand[index]
            index += 1
        return score


class Players(object):
    def __init__(self, num_players):
        if (num_players < 3) or (num_players > 5):
            raise ValueError("No Thanks requires 3 - 5 players.")
        self.num_players = num_players
        self.list_ = [Player() for _ in xrange(num_players)]
        self.cycle = cycle(self.list_)

    def next(self):
        return self.cycle.next()


class Table(object):
    def __init__(self):
        self.cards = None
        self.card = None
        self.chips = 0

    def deal(self):
        deck = range(3, 36)
        self.cards = sample(deck, 24)
        self.card = self.cards.pop()


def play_game(players, table):
    table.deal()
    while table.cards:
        player = players.next()
        player.play(table, players)


def calculate_scores(players):
    scores = {}
    for player in players.list_:
        scores[player] = player.score()
    return scores


def run_simulation(num_players=5):
    players = Players(num_players)
    table = Table()
    play_game(players, table)
    scores = calculate_scores(players)
    return scores
