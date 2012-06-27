from hand import Hand

class Player:
	'''The player has a hand, money, and makes decisions during each round, taking community card information and passing hand information to the dealer.'''
	hand = []
	community = []
	money = 100
	pbet = 0

	def __init__(self,hand=None,money=100):
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

	def bet(self,stake):
		increase = stake - self.pbet
		self.pbet = stake
		self.money -= increase
		return increase

	def fold(self):
		self.pbet = 0
		return

	def getbet(self):
		return self.pbet

	def getmoney(self):
		return self.money

	def gethand(self):
		'''Returns the cards in hand.'''
		return self.hand.getcards()
