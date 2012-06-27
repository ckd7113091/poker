from hand import Hand

class Player:
	'''The player has a hand, money, and makes decisions during each round, taking community card information and passing hand information to the dealer.'''
	hand = []
	community = []
	money = 100
	bet = 0

	def __init__(self):
		'''Basic constructor, to declare type.'''
		self.money = 100
		return

	def __init__(self,hand=None):
		'''Optional hand parameter gives a player hole cards.'''
		self.hand = Hand(hand)
		self.money = 100
		return 

	def __init__(self,hand=None,money=None):
		'''Optional money parameter defines staring money.'''
		self.hand = Hand(hand)
		self.money = money
		return

	def setcommunity(self,community):
		'''Gives a player information about the community cards.'''
		self.community = community
		return

	def getrank(self):
		'''Allows a player to determine their hand's current rank.'''
		return self.hand.rank(self.hand.highest(self.community))

	def fold(self,bet):
		self.money -= bet
		return

	def raisepot(self,deal,bet):
		deal.raisepot(self,bet)
		return

	def gethand(self):
		'''Returns the cards in hand.'''
		return self.hand.getcards()
