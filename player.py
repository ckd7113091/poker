from dealer import Dealer
from hand import Hand

class Player:
	hand = []
	community = []
	money = 100
	bet = 0

	def __init__(self):
		self.money = 100
		return

	def __init__(self,hand=None):
		self.hand = Hand(hand)
		self.money = 100
		return 

	def __init__(self,hand=None,money=None):
		self.hand = Hand(hand)
		self.money = money
		return

	def setcommunity(self,community):
		self.community = community
		return

	def getrank(self):
		return self.hand.rank(self.hand.highest(self.community))

	def fold(self,deal):
		money -= deal.fold(self)
		return

	def cc(self,deal):
		deal.cc(self)
		return

	def raisepot(self,deal,bet):
		deal.raisepot(self,bet)
		return

	def gethand(self):
		return self.hand.getcards()
