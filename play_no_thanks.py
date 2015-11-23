from itertools import cycle
from random import sample, choice

class Player(object):
	def __init__(self):
		self.hand = []
		self.chips = 11

	def play(self, table, players):
		'''
		'play' calls 'take' or 'pass_'

		This function is where game strategy can be implemented. 
		'''
		if self.chips:
			random_play = choice([self.take, self.pass_])
			random_play(table)
		else:
			self.take(table)

	def take(self, table):
		# take chips
		self.chips += table.chips
		table.chips = 0
		# take card
		self.hand.append(table.card)
		self.hand.sort()
		table.card = table.cards.pop()

	def pass_(self, table):
		self.chips -= 1
		table.chips += 1

	def score(self):
		score = -chips
		index = 0
		while index < len(self.hand):
			if index != 0:
				if self.hand[index-1] == self.hand[index]-1:
					continue
			else:
				score += self.hand[index]
		return score

class Players(object):
	def __init__(self, num_players):
		if (num_players < 3) or (num_players > 5):
			raise ValueError("No Thanks requires 3 - 5 players.")
		self.num_players = num_players
		self._players = [Player() for _ in xrange(num_players)]
		self.cycle = cycle(self._players)

	def next(self):
		return self.cycle.next()

class Table(object):
	def __init__(self):
		self.cards = None
		self.card = None
		self.chips = 0

	def deal(self):
		cards = range(3, 36)
		dealt_cards = sample(cards, 24)
		self.cards = dealt_cards
		self.card = self.cards.pop()

def play_game(players, table):
	while table.cards:
		player = players.next()
		player.play(table, players)

if __name__ == '__main__':
	num_players = input('How many players?')
	players = Players(num_players)
	table = Table()
	table.deal()
	play_game(players, table)
	print 'Done'



