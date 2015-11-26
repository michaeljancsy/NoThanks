"""No Thanks core elements"""

from itertools import cycle
from random import sample
from types import MethodType
from strategies import default_strategy


class Player(object):
    """Represents a player of the game

    Attributes:
        hand: A set of integers representing a player's cards
        chips: An integer representing how many chips a player has
        play: A function which calls take or pass_

    Notes
    -----
    Strategies are implemented in strategies.py and passed to run_simulation.
    Each strategy is a function assigned to Player.play which calls self.take
    or self.pass_. By default, the player plays randomly according to
    strategies.default_strategy.
    """
    def __init__(self):
        self.hand = set()
        self.chips = 11

    play = default_strategy

    def take(self, table):
        """Takes card and chips from table and gives them to the player"""
        # take chips
        self.chips += table.chips
        table.chips = 0
        # take card
        self.hand.add(table.card)
        table.card = table.cards.pop()

    def pass_(self, table):
        """Pays one chip to the table"""
        self.chips -= 1
        table.chips += 1

    def score(self):
        """Computes the players score"""
        hand = sorted(self.hand)
        score = -self.chips
        index = 0
        while index < len(hand):
            if index == 0 or hand[index-1] != hand[index]-1:
                score += hand[index]
            index += 1
        return score


class Players(object):
    """Collection of player objects

    Parameters
    ----------
    num_players : int, optional, default: 5
        The number of players in the game

    Attributes
    ----------
    list_ : list
        Each player in the game
    cycle : itertools.cycle
        A data structure to allow continuous rotation through the players
    """
    def __init__(self, num_players=5):
        if (num_players < 3) or (num_players > 5):
            raise ValueError("No Thanks requires 3 - 5 players.")
        self.num_players = num_players
        self.list_ = [Player() for _ in xrange(num_players)]
        self.cycle = cycle(self.list_)

    def next(self):
        """Returns the next player in the cycle"""
        return self.cycle.next()


class Table(object):
    """Represents the state of the deck and overturned card

    Attributes
    ----------
    cards : list, initialized to None until deal is called.
        Represents the cards that haven't yet been turned over
    card : int, initialized to None until deal is called.
        Represents the most recently overturned card.
    chips : int, initialized to 0
        Represents the number of chips placed atop the overturned card
    """
    def __init__(self):
        self.cards = None
        self.card = None
        self.chips = 0

    def deal(self):
        """Randomly selects 24 cards from the deck and turns one over"""
        deck = range(3, 36)
        self.cards = sample(deck, 24)
        self.card = self.cards.pop()


def play_game(players, table):
    """Sets up the table and plays the game to completion"""
    table.deal()
    while table.cards:
        player = players.next()
        player.play(table, players)


def calculate_scores(players):
    """Calculates each player's score and returns in a dictionary"""
    scores = {}
    for player in players.list_:
        scores[player] = player.score()
    return scores


def set_strategies(players, strategies):
    """Binds functions from strategies to Player.play for each player"""
    if players.num_players != len(strategies):
        raise ValueError("len(strategies) must equal num_players")
    for player, strategy in zip(players.list_, strategies):
        player.play = MethodType(strategy, player, Player)


def run_simulation(num_players=5, strategies=None):
    """Runs a game from start to finish

    Allows user to set num_players and player strategies.

    Parameters
    ----------
    num_players : int, default 5
        Number of players in the simulation
    strategies : iterable, optional
        Functions to be assigned to Player.play for each player

    Returns
    -------
    scores : dict
        Each player's final score
    """
    players = Players(num_players)
    if strategies:
        set_strategies(players, strategies)
    table = Table()
    play_game(players, table)
    scores = calculate_scores(players)
    return scores
