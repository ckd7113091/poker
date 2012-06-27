from Crypto.Random.random import shuffle

class Dealer:
	'''The Dealer class handles the deck, dealing, revealing, and showdowns.'''
	deck = range(52)
	community = []
	burned = []

	def __init__(self):
		'''Simply inststantializes a deck and shuffles it.'''
		self.shuffle()
		return

	def int2card(self,n):
		'''Assigns a card and suit to every number between 0 and 51.
			Returns a tuple in the form (card, suit).'''
		suits = ['C','S','H','D']
		return (n//4+1, suits[n%4])

	def shuffle(self):
		'''Creates a new deck and uses PyCrypto to shuffle it.'''
		self.deck = range(52)
		shuffle(self.deck)
		return

	def deal(self,players):
		'''Deals the two hole cards to each player, following the circular succession required.'''
		hands = [[0 for i in range(2)] for i in range(players)]
		for i in range(players*2):
			hands[i%players][i//players] =\
				self.int2card(self.deck.pop())
		return hands

	def reveal(self,community):
		'''Pops cards into the burn pile and the community pile as appropriate. Returns the community pile.'''
		if len(community) == 0:
			self.burned.append(self.deck.pop())
			for i in range(3):
				self.community.append(self.int2card(self.deck.pop()))
			return self.community

		if len(community) < 5:
			self.burned.append(self.deck.pop())
			self.community.append(self.int2card(self.deck.pop()))
			return self.community

		return self.community

	def showdown(self,players):
		'''Compares every player's cards. Tries to break ties; in the case that this is not possible, the returned list will include all tied parties.'''
		ranks = []
		winner = 0
		tie = []

		for player in players:
			ranks.append(player.getrank())

		for i in range(len(ranks)):
			#Check the rank.
			if ranks[i][0] > ranks[winner][0]:
				winner = i
				tie = []
			elif ranks[i][0] == ranks[winner][0]:
				if ranks[i][1] > ranks[winner][1]:
					winner = i
					tie = []
				elif ranks[i][1] == ranks[winner][1]:
					tie.append(i)
		return [winner] + [i for i in tie if i != winner]
