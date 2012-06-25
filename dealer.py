from random import randint,shuffle

class Dealer:
	deck = range(52)
	community = []
	burned = []

	def __init__(self):
		self.shuffle()
		return

	def int2card(self,num):
		suits = ['C','S','H','D']
		return (num//4+1, suits[num%4])

	def shuffle(self):
		self.deck = range(52)
		shuffle(self.deck)
		return

	def deal(self,players):
		hands = [[0]*2]*players

		for i in range(players*2):
			hands[i%players][i//players] = self.int2card(self.deck.pop())
		return hands

	def reveal(self,community):
		if len(community) == 0:
			self.burned.append(self.deck.pop())
			for i in range(3):
				self.community.append(self.int2card(self.deck.pop()))
			return self.community

		if len(community) < 5:
			self.burned.append(self.deck.pop())
			self.community.append(self.int2card(self.deck.pop()))
			return self.community

		return

	def showdown(self,players):
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
