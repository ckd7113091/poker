from random import randint,shuffle

class Dealer:
	deck
	community
	burned

	def __init__(self):
		self.shuffle()
		return

	def int2card(self,num):
		suits = ['C','S','H','D']
		return (num//4+1, suits[num%4])

	def shuffle():
		deck = range(51)
		shuffle(deck)
		return

	def deal(community):
		if len(community) == 0:
			burned.append(deck.pop())
			for i in range(3):
				community.append(deck.pop())
			return community

		if len(community) < 5:
			burned.append(deck.pop())
			community.append(deck.pop())
			return community

		return

	def showdown(players):
		ranks = []
		for player in players:
			ranks.append(player.getrank())

		winner = 0
		tie = []
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
